# Cipher Encryptor Web Application

A simple web application built with Flask that allows users to encrypt text using various encryption algorithms. The app supports the following ciphers:

- **Monoalphabetic Cipher**
- **Vigenère Cipher**
- **Playfair Cipher**
- **Transposition Cipher** (Single Columnar and Double Columnar)

## Features

- Users can input plain text and choose an encryption method.
- The app encrypts the text based on the selected cipher method and displays the encrypted text.
- Supports multiple cipher types with configurable keys.
- Easy-to-use interface with a simple form for text input and key entry.

## Installation

### Prerequisites

- Python 3.x
- Flask

### Steps to run the application

1. **Clone the repository** (or create a folder for your project):
   ```bash
   git clone https://github.com/yourusername/cipher-encryptor.git
   cd cipher-encryptor
   ```

2. **Install the required dependencies**:
   Create a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Then install Flask:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

   The application will run at `http://127.0.0.1:5000/` in your browser.

## How It Works

### Available Ciphers:

1. **Monoalphabetic Cipher**:
   - A cipher where each letter of the alphabet is mapped to a different letter.
   - The user can enter any key for the cipher. The key will define how letters are mapped.

2. **Vigenère Cipher**:
   - A cipher that uses a key word to shift the letters of the plaintext.
   - Users provide the key and the app shifts the text accordingly.

3. **Playfair Cipher**:
   - A cipher that encrypts pairs of letters using a 5x5 key table.
   - Requires the user to input a keyword that will form the key table.

4. **Transposition Cipher**:
   - The text is rearranged in a specific manner, based on the columnar order.
   - The user can choose between single or double columnar transposition.

## Files Structure

The project has the following structure:

```
cipher-encryptor/
├── app.py              # Main Flask application
├── templates/          # Folder for HTML templates
│   ├── index.html      # Input form page
│   └── result.html     # Page to display encrypted text
└── static/             # Folder for static files like CSS
    └── style.css       # Stylesheet for the app
```

## Example Usage

1. Open the app in your browser (`http://127.0.0.1:5000/`).
2. Enter the text you wish to encrypt.
3. Select the cipher type.
4. Enter the required key for encryption.
5. Press the "Encrypt" button.
6. The encrypted text will be displayed on the result page.

## Contributing

If you want to contribute to the project, feel free to fork the repository and create a pull request with improvements, bug fixes, or new features. You can also report issues using the GitHub Issues page.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
