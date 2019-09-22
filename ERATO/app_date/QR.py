from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
import pyqrcode
import urllib.parse

secretkey="tcrtrtgvfbmhgfbjujgmbgfc"

def generateQR(id):
    code=encode(secretkey,id)
    baseurl='http://192.168.0.10:8000/'#cambiar localhost por tu ip en la red

    url = pyqrcode.create(baseurl+'QRcheck/'+code)
    url.svg('assets/QR/'+id+'.svg', scale=8)
    return code

def encode(password,message):
    cipher = encrypt(password, message)
    encoded_cipher = b64encode(cipher)
    return urllib.parse.quote(encoded_cipher.decode("utf-8"),safe='').replace('%2F','%252F')


def decode(password,message):
    message=urllib.parse.unquote(message)
    cipher = b64decode(message)
    plaintext = decrypt(password, cipher)
    return plaintext.decode("utf-8")
