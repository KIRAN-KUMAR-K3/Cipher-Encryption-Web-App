from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# -------------------- MONOALPHABETIC CIPHER --------------------
def monoalphabetic_encrypt(text, key):
    return ''.join(key[ord(c) - ord('A')] if c.isalpha() else c for c in text.upper())

# -------------------- VIGENÈRE CIPHER --------------------
def vigenere_encrypt(text, key):
    text, key = text.upper(), key.upper()
    return ''.join(chr((ord(t) + ord(k) - 2 * ord('A')) % 26 + ord('A'))
                   if t.isalpha() else t
                   for t, k in zip(text, (key * (len(text) // len(key) + 1))[:len(text)]))

# -------------------- PLAYFAIR CIPHER --------------------
def preprocess_text(text):
    text = ''.join(filter(str.isalpha, text)).upper()
    if len(text) % 2 != 0:
        text += 'X'  # Padding
    return text

def create_key_table(key):
    key = ''.join(sorted(set(key.upper()), key=key.index)) + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = ''.join(sorted(set(key), key=key.index))
    return [key[i:i+5] for i in range(0, 25, 5)]

def find_position(char, key_table):
    for i, row in enumerate(key_table):
        for j, c in enumerate(row):
            if char == c:
                return i, j
    return None

def playfair_encrypt(text, key):
    text = preprocess_text(text)
    key_table = create_key_table(key)
    pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
    encrypted = ""
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_table)
        row2, col2 = find_position(pair[1], key_table)
        if row1 == row2:
            encrypted += key_table[row1][(col1 + 1) % 5]
            encrypted += key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted += key_table[(row1 + 1) % 5][col1]
            encrypted += key_table[(row2 + 1) % 5][col2]
        else:
            encrypted += key_table[row1][col2]
            encrypted += key_table[row2][col1]
    return encrypted

# -------------------- HILL CIPHER --------------------
def hill_encrypt(text, key_matrix):
    text = preprocess_text(text)
    n = key_matrix.shape[0]
    while len(text) % n != 0:
        text += 'X'
    text_vector = np.array([ord(c) - ord('A') for c in text]).reshape(-1, n).T
    encrypted_vector = (np.dot(key_matrix, text_vector) % 26).T.flatten()
    return ''.join(chr(c + ord('A')) for c in encrypted_vector)

# -------------------- ROUTES --------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    cipher_type = request.form.get('cipherType')
    text = request.form.get('text', '').strip()
    key = request.form.get('key', '').strip()
    hill_key = request.form.get('hillKey', '').strip()

    if not text:
        return render_template('result.html', result="Error: Input text cannot be empty!")

    try:
        if cipher_type == 'monoalphabetic':
            mono_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
            result = monoalphabetic_encrypt(text, mono_key)

        elif cipher_type == 'vigenere':
            result = vigenere_encrypt(text, key)

        elif cipher_type == 'playfair':
            result = playfair_encrypt(text, key)

        elif cipher_type == 'hill':
            hill_key_values = list(map(int, hill_key.split()))
            if len(hill_key_values) != 9:
                raise ValueError("Hill Cipher Key must be a 3x3 matrix (9 integers).")
            hill_matrix = np.array(hill_key_values).reshape(3, 3)
            result = hill_encrypt(text, hill_matrix)

        else:
            result = "Error: Invalid cipher type selected."

    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('result.html', result=result)

# -------------------- MAIN --------------------
if __name__ == '__main__':
    app.run(debug=True)

