from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
app = Flask(__name__)


#caesar cipher algorithm
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods = ["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text'] # type: ignore
    key = int(data['key']) # type: ignore
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypt_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods = ["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']  # type: ignore
    key = int(data['key'])  # type: ignore
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypt_message': decrypted_text})


#vigenere cipher algorithm
vigenere_cipher = VigenereCipher()

@app.route("/api/vigenere/encrypt", methods = ["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text'] # type: ignore
    key = data['key'] # type: ignore
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypt_text': encrypted_text})

@app.route("/api/vigenere/decrypt", methods = ["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']  # type: ignore
    key = data['key'] # type: ignore
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypt_text': decrypted_text})


#rail_fence cipher algorithm
railfence_cipher = RailFenceCipher()
@app.route("/api/railfence/encrypt", methods = ["POST"])
def encrypt():
    data = request.json
    plain_text = data['plain_text'] # type: ignore
    key = int(data['key']) # type: ignore
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypt_text': encrypted_text})
@app.route("/api/railfence/decrypt", methods = ["POST"])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text'] # type: ignore
    key = int(data['key']) # type: ignore
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypt_text': decrypted_text})

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)