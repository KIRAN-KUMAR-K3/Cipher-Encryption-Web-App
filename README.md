
# Cipher Encryption Web App

## Overview
The **Cipher Encryption Web App** is a simple web application that allows users to encrypt and decrypt messages using various encryption algorithms. This project is built with Python using the Flask framework, allowing users to interact with the app through a clean and user-friendly web interface.

### Features:
- Encrypt text using different ciphers (Caesar Cipher, Substitution Cipher, etc.)
- Decrypt previously encrypted text
- Web interface for easy use
- Python backend with Flask
- Lightweight and responsive design

---

## Requirements

To run this project, you'll need to have the following installed:

- **Python 3.x**
- **pip** (Python package installer)

### Python Libraries:

1. Flask
2. (Other libraries if used in your project)

These libraries can be installed using the following command:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
├── app.py                 # Main Python file to run the Flask app
├── requirements.txt       # List of dependencies for the project
├── static/                # Contains static files like CSS
│   └── style.css          # Custom styles for the frontend
└── templates/             # HTML templates
    ├── index.html         # Main page of the web app
    └── result.html        # Page to display the encryption/decryption result
```

---

## Setup

### Clone the repository:

```bash
git clone https://github.com/KIRAN-KUMAR-K3/Cipher-Encryption-Web-App.git
cd Cipher-Encryption-Web-App
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the app:

To start the web app, simply run the following command:

```bash
python app.py
```

This will start the Flask development server. You can access the app by opening your browser and going to `http://127.0.0.1:5000/`.

---

## How to Use

1. Open the app in your browser (`http://127.0.0.1:5000/`).
2. On the homepage, you can input a message that you want to encrypt or decrypt.
3. Select the desired cipher method (e.g., Caesar Cipher, Substitution Cipher).
4. Enter the key or shift value if required.
5. Click the **Encrypt** or **Decrypt** button.
6. The encrypted or decrypted message will be displayed on the result page.

---

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---