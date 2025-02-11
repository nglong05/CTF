```py
from flask import Flask, request, redirect, render_template_string
import sys
import os
import bcrypt
import urllib.parse

app = Flask(__name__)
app.secret_key = os.urandom(16);
# This is super strong! The password was generated quite securely. Here are the first 70 bytes, since you won't be able to brute-force the rest anyway...
# >>> strongpw = bcrypt.hashpw(os.urandom(128),bcrypt.gensalt())
# >>> strongpw[:71]
# b'\xec\x9f\xe0a\x978\xfc\xb6:T\xe2\xa0\xc9<\x9e\x1a\xa5\xfao\xb2\x15\x86\xe5$\x86Z\x1a\xd4\xca#\x15\xd2x\xa0\x0e0\xca\xbc\x89T\xc5V6\xf1\xa4\xa8S\x8a%I\xd8gI\x15\xe9\xe7$M\x15\xdc@\xa9\xa1@\x9c\xeee\xe0\xe0\xf76'
app.ADMIN_PW_HASH = b'$2b$12$8bMrI6D9TMYXeMv8pq8RjemsZg.HekhkQUqLymBic/cRhiKRa3YPK'
FLAG = open("flag.txt").read();

@app.route('/source')
def source():
    return open(__file__).read()

@app.route('/', methods=["GET"])
def index():

    username = request.form.get("username", None)
    password = request.form.get("password", None)

    if username and password:

        username = urllib.parse.unquote_to_bytes(username)
        password = urllib.parse.unquote_to_bytes(password)

        if username != b"admin":
            return "Wrong user!"

        if len(password) > 128:
            return "Password too long!"

        if not bcrypt.checkpw(password, app.ADMIN_PW_HASH):
            return "Wrong password!"

        return f"""Congrats! It appears you have successfully bf'ed the password. Here is your {FLAG}"""
    
    # Use f-string formatting within the template string
    template_string = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Bfail</title>
    </head>
    <body>
        <h1>Login to get my secret, but 'B'-ware of the strong password!</h1>
        <form action="/" method="post">
            <label for="username">Username:</label>
            <input type="text" name="username"  placeholder="admin">
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password">
            <br>
            <button type="submit">Login</button>
        </form>
    <!-- See my <a href="/source">Source</a> -->
    </body>
    </html>
    """

    return render_template_string(template_string)

if __name__ == '__main__':
   app.run(debug=False, host="0.0.0.0", port="8080", threaded=True)
```