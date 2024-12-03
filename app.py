from flask import Flask, render_template, request

app = Flask(__name__)

# Helper function for the Mono-Alphabetic Substitution Cipher
def monoalphabetic_substitution(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    table = dict(zip(alphabet, key))  # Create a substitution table from the key
    encrypted_text = ''.join([table.get(char, char) for char in text.upper()])
    return encrypted_text

# Helper function for the Vigenère Cipher (Polyalphabetic Substitution)
def vigenere_cipher(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper()
    encrypted_text = []
    key_len = len(key)
    for i, char in enumerate(text.upper()):
        if char in alphabet:
            shift = alphabet.index(key[i % key_len])
            encrypted_char = alphabet[(alphabet.index(char) + shift) % 26]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Keep non-alphabetic characters unchanged
    return ''.join(encrypted_text)

# Helper function for the Playfair Cipher
def playfair_substitution(text, key):
    # Create a 5x5 Playfair matrix
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key.upper()), key=lambda x: key.index(x)))  # Removing duplicates from key
    key_matrix = key + alphabet
    key_matrix = ''.join(sorted(set(key_matrix), key=lambda x: key_matrix.index(x)))  # Final matrix string
    
    # Create a dictionary for the matrix
    matrix = {key_matrix[i]: (i // 5, i % 5) for i in range(len(key_matrix))}
    
    # Prepare the text for Playfair cipher (change J to I)
    text = text.upper().replace('J', 'I')
    if len(text) % 2 != 0:
        text += 'X'  # Add padding X if length is odd

    encrypted_text = []
    for i in range(0, len(text), 2):
        first_char = text[i]
        second_char = text[i+1]

        row1, col1 = matrix[first_char]
        row2, col2 = matrix[second_char]

        if row1 == row2:
            encrypted_text.append(key_matrix[row1*5 + (col1+1) % 5])
            encrypted_text.append(key_matrix[row2*5 + (col2+1) % 5])
        elif col1 == col2:
            encrypted_text.append(key_matrix[((row1+1) % 5)*5 + col1])
            encrypted_text.append(key_matrix[((row2+1) % 5)*5 + col2])
        else:
            encrypted_text.append(key_matrix[row1*5 + col2])
            encrypted_text.append(key_matrix[row2*5 + col1])

    return ''.join(encrypted_text)

# Helper function for the Hill Cipher
def hill_cipher(text, key):
    # 2x2 Hill cipher for simplicity
    key_matrix = [[int(key[0]), int(key[1])], [int(key[2]), int(key[3])]]
    text = text.upper().replace(' ', '')
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted_text = []

    for i in range(0, len(text), 2):
        chunk = text[i:i + 2]
        if len(chunk) < 2:
            chunk += 'X'  # Add padding X if chunk is incomplete
        chunk_vector = [alphabet.index(chunk[0]), alphabet.index(chunk[1])]
        encrypted_chunk = [
            (key_matrix[0][0] * chunk_vector[0] + key_matrix[0][1] * chunk_vector[1]) % 26,
            (key_matrix[1][0] * chunk_vector[0] + key_matrix[1][1] * chunk_vector[1]) % 26
        ]
        encrypted_text.append(alphabet[encrypted_chunk[0]] + alphabet[encrypted_chunk[1]])
    
    return ''.join(encrypted_text)

# Transposition Cipher - Single Columnar
def single_columnar_transposition(text, key):
    # Create a table with columns based on the key
    num_cols = len(key)
    num_rows = len(text) // num_cols
    remainder = len(text) % num_cols
    padded_text = text + 'X' * (num_cols - remainder) if remainder != 0 else text
    grid = [padded_text[i:i + num_cols] for i in range(0, len(padded_text), num_cols)]

    # Rearrange columns based on the key
    key_order = sorted(list(range(num_cols)), key=lambda k: key[k])
    transposed_text = ''.join([''.join([grid[row][key_order[col]] for row in range(num_rows)]) for col in range(num_cols)])

    return transposed_text

# Transposition Cipher - Double Columnar
def double_columnar_transposition(text, key1, key2):
    # First columnar transposition using key1
    step1 = single_columnar_transposition(text, key1)
    # Then second columnar transposition using key2
    return single_columnar_transposition(step1, key2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    cipher_type = request.form['cipher_type']
    cipher_option = request.form['cipher_option']
    input_text = request.form['input_text']
    key = request.form['key']
    
    if cipher_type == 'substitution':
        if cipher_option == 'monoalphabetic':
            output_text = monoalphabetic_substitution(input_text, key)
        elif cipher_option == 'vigenere':
            output_text = vigenere_cipher(input_text, key)
        elif cipher_option == 'playfair':
            output_text = playfair_substitution(input_text, key)
        elif cipher_option == 'hill':
            output_text = hill_cipher(input_text, key)
    elif cipher_type == 'transposition':
        if cipher_option == 'single_columnar':
            output_text = single_columnar_transposition(input_text, key)
        elif cipher_option == 'double_columnar':
            key2 = request.form['key2']  # Additional key for double columnar transposition
            output_text = double_columnar_transposition(input_text, key, key2)

    return render_template('result.html', input_text=input_text, output_text=output_text, cipher_type=cipher_type, cipher_option=cipher_option)

if __name__ == '__main__':
    app.run(debug=True)
