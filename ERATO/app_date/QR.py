from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
import pyqrcode
import urllib.parse
import hashlib
from ERATO.settings import BASE_DIR

secretkey="tcrtrtgvfbmhgfbjujgmbgfc"

def generateQR(id,noise,request):
    code=hashlib.sha256(bytes(id+noise,'utf-8')).hexdigest()
    baseurl=request.META['HTTP_HOST']+'/qrcheck/'+id+'/'+str(code)
    url = pyqrcode.create(baseurl)
    result_path = BASE_DIR+'/assets/QR/'+id+'.png'
    url.png(result_path, scale=8, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    print(result_path)
    return result_path

def encode(password,message):
    cipher = encrypt(password, message)
    encoded_cipher = b64encode(cipher)
    return urllib.parse.quote(encoded_cipher.decode("utf-8"),safe='').replace('%2F','%252F')


def decode(password,message):
    message=urllib.parse.unquote(message)
    cipher = b64decode(message)
    plaintext = decrypt(password, cipher)
    return plaintext.decode("utf-8")
