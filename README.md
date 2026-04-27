# QR Code Generator System

A Flask-based web application designed to generate and manage secure entry QR codes for guests. This project was developed to streamline check-in processes while maintaining a high standard of administrative control and security.

## 🚀 Key Features
* **Dynamic Branding:** Update establishment name via settings panel
* **Rich Text Emails:** WYSIWYG editor using Quill.js
* **Automated Dispatch:** Generates and sends QR codes directly to guests
* **Security Override:** Emergency access with admin notifications
* **Environment-Based Configuration:** Secure handling of sensitive credentials via environment variables
* **One-Click Launch (Windows Only):** Run the application using run.bat

## 🛠️ Tech Stack
* **Backend:** Python 3.10+ (Flask)
* **Frontend:** HTML5, CSS3, JavaScript (Quill.js)
* **Email Service:** SMTP (configurable via .env)
* **Environment:** Cross-platform support (Windows/Linux/MacOS)

## 📌 Deployment Note
This project is designed for local or internal deployment environments. It is not currently hosted for public production use.

## 📁 Repository Structure

```
qr-generator/
├── app.py
├── requirements.txt
├── .env.example
├── run.bat
├── README.md
├── SETUP.md
|
├── templates/
│   ├── index.html
│   └── settings.html
|
└── static/
    ├── styles.css
    └── qrcodes/
```

### File/Folder Description

- `app.py` – Main Flask application containing routes and core logic.
- `requirements.txt` – List of Python dependencies.
- `.env.example` – Template for environment variables (copy as `.env` and configure).
- `templates/` – HTML templates for the user interface.
- `static/` – Static assets including CSS and generated QR code images.
- `run.bat` – One-click launcher to automatically set up the environment, start the Flask server, and open the application in the browser (Windows only).
- `SETUP.md` – Step-by-step installation and local setup guide.
- `README.md` – Project overview and documentation.