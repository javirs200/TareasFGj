from flask import Flask, request
#PyCryptodome
from Crypto.Cipher import AES
import random
from Crypto.Util.Padding import pad
from binascii import hexlify as heg
import subprocess
import base64
import binascii
import pickle
app = Flask(__name__)

first_key = b""
second_key = b""

FLAG = str(int(heg(heg(heg(b"the code secret is 'i_eat_a_lot_of_pancakes' !!!!"))).decode('utf-8')) ^ 15).encode()

token_auth = "i_eat_a_lot_of_pancakes"

def encrypt(plaintext, a, b):
    cipher = AES.new(a, mode=AES.MODE_ECB)
    ct = cipher.encrypt(pad(plaintext, 16))
    cipher = AES.new(b, mode=AES.MODE_ECB)
    ct = cipher.encrypt(ct)
    return ct.hex()

def generateKey():
    global first_key, second_key
    first_key = (str(random.randint(0, 99999)).zfill(5)*4)[:16].encode()
    second_key = (str(random.randint(0, 99999)).zfill(5)*4)[:16].encode()
    print(second_key)

@app.route("/")
def home():
    a = """
	<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Secured dicci API</title>
        <!-- cache -->
        <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Expires" content="0">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

        <style>
            :root {
                --background: #f4f5ff;
                --primary: #1320d9;
                --black: #030303;
                --light-black: #252525;
                --white: #ffffff;
            }
            html, body {
                background-color: var(--background);
            }
            .topnav {
                overflow: hidden;
                background-color: var(--primary);
                color: white;
                padding: 15px 20px;
                font-size: 17px;
            }
            .prettyprint {
                padding: 8px;
                background-color: #f7f7f9;
                border: 1px solid #e1e1e8;
                margin: 0 0 10px;
                line-height: 1.42857143;
                color: #333;
                word-break: break-all;
                border-radius: 4px;
                font-family: var(--bs-font-monospace);
            }
        </style>

        <link href="https://hackrocks.com/assets/images/favicon.png" rel="shortcut icon" type="image/x-icon">
        <link href="https://hackrocks.com/assets/images/webclip.png" rel="apple-touch-icon">
    </head>
    <body>
        <div class="topnav">
            <div class="container">
                Secured dicci API
            </div>
        </div>
        <div class="container mt-4">
            <h1>The Parameters</h1>
            <div class="prettyprint">
                <b>GET </b> /admin_key<br><br>
                <b>GET </b> /api/enc_data?plain=PLAINTEXT_HERE
            </div>
            <p class="m-0"><i>Our API and Cryptography mechanism is very strong that no one cannot break it </i></p>
        </div>
    </body>
</html>
    """
    return a

@app.route('/admin_key', methods=['GET'])
def ret_all():
    try:
        return encrypt(FLAG, first_key, second_key) + "\n\n"
    except Exception as b:
        print(b)
        return "<p>admin_key_error</p>"


@app.route("/api/enc_data", methods=['GET'])
def enc_data():
    try:
            preparse = request.args.get("plain")
            temp = preparse.encode('utf-8')
            temp = encrypt(temp, first_key, second_key)
            return temp + "\n\n"
    except Exception as a:
        print(a)
        return "<p> Encryption Error!<p>"

@app.route("/panel", methods=['GET'])
def henlo():
    try:
        key = request.args.get("key")
        code = request.args.get("code")
        if key == token_auth:
            temp = code.encode()
            c = binascii.unhexlify(temp)
            if c != None:
                pickle.loads(c)
                return "<p> loaded ! </p>"
    except Exception as e:
        print(e)
        return "<p>panel error</p>"


if __name__ == '__main__':
    generateKey()
    app.run(host="0.0.0.0", port=5000)
