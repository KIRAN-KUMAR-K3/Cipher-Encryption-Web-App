
# Cipher Encryption Web App

This is a web application built using Flask that allows users to encrypt text using various substitution and transposition ciphers. The application provides a user-friendly interface to choose between different cipher types, input plaintext, and get the corresponding encrypted output.

## Features

### Substitution Ciphers:
- **Monoalphabetic Cipher**
- **Polyalphabetic Cipher (Vigenère Cipher)**
- **Playfair Cipher**
- **Hill Cipher**

### Transposition Ciphers:
- **Single Columnar Transposition**
- **Double Columnar Transposition**

### Interactive Interface:
- Users can choose between the different cipher types.
- The application supports both substitution and transposition cipher types.
- It provides an option to input the required cipher key for encryption.
- Displays the encrypted text once the encryption process is complete.

## Technologies Used
- **Python 3.x**: Programming language.
- **Flask**: Web framework to run the application.
- **HTML/CSS**: For the front-end design of the app.
- **JavaScript**: For dynamic UI behavior.

## Requirements

To run this project, you need the following installed:

- Python 3.x
- Flask

### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/KIRAN-KUMAR-K3/Cipher-Encryption-Web-App.git
cd Cipher-Encryption-Web-App
```

### Step 2: Install the required dependencies

Install Flask and any other dependencies via pip:

```bash
pip install -r requirements.txt
```

### Step 3: Run the application

To start the Flask application, run the following command:

```bash
python app.py
```

The app will be running at `http://127.0.0.1:5000/`.

## How to Use

1. **Choose a Cipher**: On the home page, select the cipher type (either Substitution or Transposition).
2. **Enter Text**: Input the text you want to encrypt.
3. **Select Cipher Parameters**: 
   - For substitution ciphers (like Vigenère, Monoalphabetic), you may need to enter a key.
   - For transposition ciphers, you may need to provide the key length or the number of columns.
4. **Click "Encrypt"**: Once you input the required data, click on the Encrypt button.
5. **View Result**: The encrypted text will be displayed on the results page.

## Project Structure

```
├── app.py                # Main Flask application code
├── requirements.txt      # List of required Python libraries
├── static/
│   └── style.css         # CSS for styling the app
└── templates/
    ├── index.html        # Home page for the app (user interface)
    └── result.html       # Page to display the encrypted result
```

## Contributing

Contributions are welcome! If you find any issues or want to add new cipher techniques, feel free to open a pull request or create an issue.

## License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more details.

