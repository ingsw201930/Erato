from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
import pyqrcode
import urllib.parse

secretkey="tcrtrtgvfbmhgfbjujgmbgfc"

def generateQR(id,noise,request):
    code=hash(id+noise)
    baseurl=request.META['HTTP_HOST']+'/QRcheck/'+id+'/'+str(code)
    url = pyqrcode.create(baseurl)
    url.png('assets/QR/'+id+'.png', scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    return 'assets/QR/'+id+'.png'

def encode(password,message):
    cipher = encrypt(password, message)
    encoded_cipher = b64encode(cipher)
    return urllib.parse.quote(encoded_cipher.decode("utf-8"),safe='').replace('%2F','%252F')


def decode(password,message):
    message=urllib.parse.unquote(message)
    cipher = b64decode(message)
    plaintext = decrypt(password, cipher)
    return plaintext.decode("utf-8")
