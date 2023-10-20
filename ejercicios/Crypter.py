# Se debe ejecutar pip install pycryptodomex
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import base64
import json

def encrypt_request(request, key):
    cipher = AES.new(key.encode(), AES.MODE_CBC)
    encrypted_bytes = cipher.encrypt(pad(json.dumps(request).encode(), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode()
    encrypted_request = base64.b64encode(encrypted_bytes).decode()
    return {'iv': iv, 'encrypted_request': encrypted_request}

def decrypt_request(encrypted_request, key):
    iv = base64.b64decode(encrypted_request['iv'])
    encrypted_bytes = base64.b64decode(encrypted_request['encrypted_request'])
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    decrypted_bytes = unpad(cipher.decrypt(encrypted_bytes), AES.block_size)
    decrypted_request = json.loads(decrypted_bytes.decode())
    return decrypted_request

# Ejemplo de uso

request = {'name': 'John Doe', 'age': 25, 'email': 'johndoe@example.com'}
key = '123456789012345678901234'


encrypted_request = encrypt_request(request, key)
print('Solicitud encriptada:', encrypted_request)


decrypted_request = decrypt_request(encrypted_request, key)
print('Solicitud desencriptada:', decrypted_request)