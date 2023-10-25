import base64
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
import json
 
class AESEncyption:
     secret_key = b"tK5UTui+DPh8lIlBxya5XVsmeDCoUl6vHhdIESMB6sQ="
     salt = b"QWlGNHNhMTJTQWZ2bGhpV3U="
     iv = b"bVQzNFNhRkQ1Njc4UUFaWA=="
 
     @staticmethod
     def encrypt(str_to_encrypt):
        try:
            str_to_encrypt += ((16 - len(str_to_encrypt) % 16)*'\a')
            iv_parameter_spec = base64.b64decode(AESEncyption.iv)
            salt = base64.b64decode(AESEncyption.salt)
            secret_key = PBKDF2(AESEncyption.secret_key, salt, dkLen=32, count=10000)
            cipher = AES.new(secret_key, AES.MODE_CBC, iv_parameter_spec)
            encrypted = cipher.encrypt(str_to_encrypt.encode('utf-8'))
            return base64.b64encode(encrypted).decode('utf-8')
        except Exception as e:
            print("Error while encrypting:", e)
        return None
     
     @staticmethod
     def decrypt(strToDecrypt):
        try:
            iv_parameter_spec = base64.b64decode(AESEncyption.iv)
            salt = base64.b64decode(AESEncyption.salt)
            secret_key = PBKDF2(AESEncyption.secret_key, salt, dkLen=32, count=10000)
            cipher = AES.new(secret_key, AES.MODE_CBC, iv_parameter_spec)
            decrypted = cipher.decrypt(base64.b64decode(strToDecrypt))
            return decrypted.decode().strip()
            #return decrypted
        except Exception as e:
             print("Error while decrypting:", e)
        return None
     
 
if __name__ == '__main__':
   encript = AESEncyption()
   ciph_text = '''
   BJi38+lDvqOlikTq9N4hP3mEs2BkOIIcvDKZ12UEbGA/z/G9jqAcKjV10frYl6VlHwTDh82u1Lm3
   yx73TCxhUaw/7R+BxyUfm+Ipwee1Z8D7lhtEHXq5ODT64A+L0coGEZOQqQEp8pSjlq/iG6LjyNvh
   b0fYfcr+3TtxV1a2GWpYzp4k4AcCIuUhcNIlCS53AMZp9NV5omepHV7r48xN2ecFPTY+qt4QCTVx
   latSIsb5sUKAZLP75HYtqdMCE1a+M6ca/At+73LdJpMVleRRZZESMjLh6zOoq9jQpXKiWuTbLBV+
   s0mn5MPzCI3+j8ct7CVcBmwwD/8lQ+1IcdrRLiWP/xdC82CEQhMUyIpA1307XBqTwBLDPGYd2Msh
   /a2pqrHmMCD7dPtwO2J8rgrxPAPj0HMH3bXVgi/yj1gFcvz2dZCTtazRKn8iaEAd7idTIXrAoYlt
   beJDXeYU3Lymdg=='''
   ee = encript.decrypt(ciph_text)
   print("DECRYPT: ", ee)
