from flask import Flask, render_template, request

app = Flask(__name__)

# -------------------- MONOALPHABETIC CIPHER --------------------
def monoalphabetic_encrypt(text, key):
    encrypted = ''.join(key[ord(c) - ord('A')] if c.isalpha() else c for c in text.upper())
    return encrypted

def monoalphabetic_decrypt(text, key):
    inverse_key = {v: k for k, v in enumerate(key)}
    decrypted = ''.join(chr(inverse_key[c] + ord('A')) if c.isalpha() else c for c in text.upper())
    return decrypted

# -------------------- VIGENÈRE CIPHER --------------------
def vigenere_encrypt(text, key):
    text, key = text.upper(), key.upper()
    encrypted = ''.join(chr((ord(t) + ord(k) - 2 * ord('A')) % 26 + ord('A'))
                        if t.isalpha() else t
                        for t, k in zip(text, (key * (len(text) // len(key) + 1))[:len(text)]))
    return encrypted

def vigenere_decrypt(text, key):
    text, key = text.upper(), key.upper()
    decrypted = ''.join(chr((ord(t) - ord(k) + 26) % 26 + ord('A'))
                        if t.isalpha() else t
                        for t, k in zip(text, (key * (len(text) // len(key) + 1))[:len(text)]))
    return decrypted

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
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    encrypted = ""
    for pair in pairs:
        row1, col1 = find_position(pair[0], key_table)
        row2, col2 = find_position(pair[1], key_table)
        if row1 == row2:  # Same row
            encrypted += key_table[row1][(col1 + 1) % 5]
            encrypted += key_table[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted += key_table[(row1 + 1) % 5][col1]
            encrypted += key_table[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted += key_table[row1][col2]
            encrypted += key_table[row2][col1]
    return encrypted

# -------------------- TRANSPOSITION CIPHER --------------------
def transpose_encrypt(text, method):
    text = text.replace(" ", "").upper()
    if method == "single_columnar":
        return ''.join(sorted(text))  # Single columnar transposition
    elif method == "double_columnar":
        return ''.join([text[i::2] for i in range(2)])  # Double columnar transposition
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        cipher_type = request.form['cipher_type']
        key = request.form['key']
        transposition_type = request.form.get('transposition_type')

        if cipher_type == "monoalphabetic":
            mono_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
            encrypted_text = monoalphabetic_encrypt(text, mono_key)
        elif cipher_type == "vigenere":
            encrypted_text = vigenere_encrypt(text, key)
        elif cipher_type == "playfair":
            encrypted_text = playfair_encrypt(text, key)
        elif cipher_type == "transposition":
            encrypted_text = transpose_encrypt(text, transposition_type)
        
        return render_template('result.html', encrypted_text=encrypted_text)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
