from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

app = Flask(__name__)

key = b'b3698341dd502d7e'  # 16-byte key for AES-128
iv = b'2870722839122095'   # 16-byte IV for CBC mode

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data')
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(data.encode(), AES.block_size))
    hex_output = binascii.hexlify(ciphertext).decode()
    
    return jsonify({'encrypted_data': hex_output})

if __name__ == '__main__':
    app.run(debug=True, port=9080, host='0.0.0.0')