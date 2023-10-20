import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad
import hashlib

def get_private_key(secretKey, salt):
    # _prf = lambda p,s: HMAC.new(p, s, SHA256).digest()
    # private_key = PBKDF2(secretKey, salt.encode(), dkLen=32,count=65536, prf=_prf )
    # above code is equivalent but slow
    key = hashlib.pbkdf2_hmac('SHA256', secretKey.encode(), salt.encode(), 65536, 32)
    # KeySpec spec = new PBEKeySpec(secretKey.toCharArray(), salt.getBytes(), 65536, 256);
    return key

def encrypt(message, salt, secretKey):
    private_key = get_private_key(secretKey, salt)
    message = pad(message.encode(), AES.block_size)
    iv = "\x00"*AES.block_size  # 128-bit IV
    cipher = AES.new(private_key, AES.MODE_CBC, iv.encode())
    return base64.b64encode(cipher.encrypt(message))

def decrypt(enc, salt, secretKey):
    # _prf = lambda p,s: HMAC.new(p, s, SHA256).digest()
    # private_key = PBKDF2(secretKey, salt.encode(), dkLen=32,count=65536, prf=_prf )
    private_key = get_private_key(secretKey, salt)
    enc = base64.b64decode(enc)
    iv = "\x00"*AES.block_size
    cipher = AES.new(private_key, AES.MODE_CBC, iv.encode())
    return unpad(cipher.decrypt(enc), AES.block_size).decode('utf-8')



secretKey = "Secret"
salt = "tJHnN5b1i6wvXMwzYMRk"
plainText = "Federico Martinez Escamilla"

enc_datta = encrypt(plainText, salt, secretKey)
print(f"Encrypted: {enc_datta}")
# Encrypted: 0JrZdg9YBRshfTdr1d4zwQ==

cipher = enc_datta # Cipher from java
decrypted = decrypt(cipher, salt, secretKey)
print(f"Decrypted: {decrypted}" )
# Decrypted: England