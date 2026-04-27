from flask import Flask, render_template, request, redirect, url_for, session
import qrcode
import os
import datetime
import random
import string
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_default_key")

# Configuration
QR_FOLDER = os.getenv("QR_FOLDER", "static/qrcodes")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
OVERRIDE_KEY = os.getenv("OVERRIDE_KEY")

os.makedirs(QR_FOLDER, exist_ok=True)

def send_email(subject, body_html, recipient_email, qr_filepath=None):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body_html, "html")) # Support for Rich Text

    if qr_filepath:
        try:
            with open(qr_filepath, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(qr_filepath)}")
                msg.attach(part)
        except Exception as e:
            print(f"Attachment error: {e}")

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), int(os.getenv("SMTP_PORT")), context=context) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        return True
    except Exception as e:
        print(f"SMTP error: {e}")
        return False

def generate_unique_filename():
    return f"qr_{int(datetime.datetime.now().timestamp())}.png"

def generate_random_numbers(length):
    number = string.digits
    numbers = ''.join(random.choices(number, k=length))
    while '00' in numbers or '11' in numbers:
        numbers = numbers.replace('00', ''.join(random.choices(number, k=2)), 1)
        numbers = numbers.replace('11', ''.join(random.choices(number, k=2)), 1)
    return numbers

def format_time(time_str):
    military_time = time_str.replace(":", "")
    hour = int(military_time[:2])
    minute = military_time[2:]
    suffix = "AM" if hour < 12 else "PM"
    display_hour = hour if 1 <= hour <= 12 else abs(hour - 12)
    if display_hour == 0: display_hour = 12
    return f"{display_hour}:{minute} {suffix}", military_time

def generate_qr_code(start_date, end_date, check_in, check_out):
    s_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").strftime("%m%d%y")
    e_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").strftime("%m%d%y")
    qr_string = f"{generate_random_numbers(2)}00{s_date}{check_in}99{e_date}{check_out}11{generate_random_numbers(2)}"
    
    qr = qrcode.QRCode(version=1, box_size=20, border=2)
    qr.add_data(qr_string)
    qr.make(fit=True)
    
    file_name = generate_unique_filename()
    file_path = os.path.join(QR_FOLDER, file_name)
    qr.make_image().save(file_path)
    return file_name, file_path

@app.route("/", methods=["GET", "POST"])
def index():
    qr_filename = None
    error = None
    is_override = False
    
    # Load settings
    comp = session.get('company_name', os.getenv("COMPANY_NAME"))
    subject_tpl = session.get('mail_subject', os.getenv("EMAIL_SUBJECT_WELCOME"))
    body_tpl = session.get('mail_body', os.getenv("EMAIL_BODY_WELCOME"))

    if request.method == "POST":
        if "override_qr" in request.form:
            override_path = os.path.join(QR_FOLDER, "override.png")
            qr = qrcode.QRCode(version=1, box_size=20, border=2)
            qr.add_data(OVERRIDE_KEY)
            qr.make(fit=True)
            qr.make_image().save(override_path)
            
            override_timestamp = datetime.datetime.now().strftime("%Y-%m-%d @ %I:%M:%S %p")

            email_subject = "⚠️ OVERRIDE QR Code Generated ⚠️"
            email_body = (
                f"WARNING: An OVERRIDE QR code has been generated.<br>"
                f"➢ Timestamp: {override_timestamp}<br><br>"
                f"Please verify if this action was authorized."
            )

            # {datetime.datetime.now()}
            
            send_email(email_subject, email_body, EMAIL_ADDRESS, override_path)
            qr_filename = "override.png"
            is_override = True
        else:
            start = request.form.get("start_date")
            end = request.form.get("end_date")
            email = request.form.get("email")
            
            if not all([start, end, email]):
                error = "Please fill in all fields."
            else:
                in_std, in_mil = format_time(request.form.get("check_in"))
                out_std, out_mil = format_time(request.form.get("check_out"))
                
                qr_filename, qr_path = generate_qr_code(start, end, in_mil, out_mil)
                
                # Process placeholders
                final_sub = subject_tpl.replace("{company_name}", comp)
                final_body = body_tpl.replace("{company_name}", comp)\
                                    .replace("{start_date}", start)\
                                    .replace("{check_in}", in_std)\
                                    .replace("{end_date}", end)\
                                    .replace("{check_out}", out_std)
                
                send_email(final_sub, final_body, email, qr_path)

    return render_template("index.html", qr_filename=qr_filename, error=error, is_override=is_override, company_name=comp)

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        session['company_name'] = request.form.get("company_name")
        session['mail_subject'] = request.form.get("mail_subject")
        session['mail_body'] = request.form.get("mail_body")
        return redirect(url_for('index'))
    
    return render_template("settings.html", 
                            company_name=session.get('company_name', os.getenv("COMPANY_NAME")),
                            subject=session.get('mail_subject', os.getenv("EMAIL_SUBJECT_WELCOME")),
                            body=session.get('mail_body', os.getenv("EMAIL_BODY_WELCOME")))

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)