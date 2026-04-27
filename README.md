# QR Code Generator System

A Flask-based web application designed to generate and manage secure entry QR codes for guests. This project was developed to streamline check-in processes while maintaining a high standard of administrative control and security.

## 🚀 Key Features
* **Dynamic Branding:** Change the establishment name via the settings.
* **Rich Text Emails:** Fully customizable email templates using a built-in WYSIWYG editor (Quill.js).
* **Automated Dispatch:** Generates a unique QR code and emails it directly to the guest upon form submission.
* **Security Override:** Includes a master override feature with automatic admin email notifications for emergency access.
* **Secure Configuration:** Sensitive credentials and security keys are managed via environment variables.

## 🛠️ Tech Stack
* **Backend:** Python 3.10+ (Flask)
* **Frontend:** HTML5, CSS3, JavaScript (Quill.js)
* **Environment:** Cross-platform support (Windows/Linux/MacOS)

## 📌 Deployment Note
This project is designed for local or internal deployment environments. It is not currently hosted for public production use.

## 📁 Repository Structure

```
qr-generator/
├── app.py
├── requirements.txt
├── .env.example
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
- `SETUP.md` – Step-by-step installation and local setup guide.
- `README.md` – Project overview and documentation.