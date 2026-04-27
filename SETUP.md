# QR Code Generator Setup Guide

This guide walks through installing and running the flask-based web application locally.

---

# 1. Requirements

Install:

* Python 3.10+
* pip
* Git (optional)

Verify:

```bash
python --version
pip --version
```

---

# 2. Clone or Download Project

```bash
git clone https://github.com/JRAntiojo/qr-generator.git
cd qr-generator
```

Or download ZIP and extract.

---

# 3. Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 4. Install Dependencies

Install:

```bash
pip install -r requirements.txt
```

---

# 5. Create and modify .env File

Create `.env` in project root:

```bash
cp .env.example .env
# Fill in all necessary variables and generate SECRET_KEY
```

---

## Gmail Note

If using Gmail:

Use an **App Password**, not your normal login password.

Generate under:

Google Account → Security → App Passwords

---

# 6. Run Application

```bash
python app.py
```

Runs on:

```text
http://localhost:5000
```

---

# 7. Test Features

## Guest QR Test

* Enter dates/times
* Enter your email
* Click Generate & Send QR Code

Verify:

* QR appears
* Download works
* Email received

---

## Override Test

Click:

```text
Admin Override
```

Verify:

* Override QR generated
* Alert email received

# Troubleshooting

## SMTP Authentication Error

Check:

* Email/password
* App password
* SMTP server/port

---

## QR Not Saving

Verify:

```bash
static/qrcodes/
```

exists and writable.

---

## Environment Variables Not Loading

Install:

```bash
pip install python-dotenv
```

Verify `.env` is in same folder as `app.py`.

---

## Port Already In Use

Change:

```python
app.run(port=5001)
```

or stop existing process.

---

# Example Startup Workflow

```bash
cd qr-generator
venv\Scripts\activate
python app.py
```

Open:

```text
http://localhost:5000
```

---

Setup complete.
