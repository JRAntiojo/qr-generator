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

## 📁 Repository Structure
- `app.py`: Main application logic and routing.
- `static/`: Contains CSS and generated QR code images.
- `templates/`: HTML templates for the UI.
- `.env.example`: Template for local configuration.

```
qr-generator/
|
├── app.py
├── requirements.txt
├── .env.example             ← copy to .env and fill in
├── README.md
├── SETUP.md
├── templates/
│   ├── index.html
│   └── settings.html
└── static/
    ├── styles.css
    └── qrcodes/
```