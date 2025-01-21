## Description
Two endpoints are available :

POST : /web-serveur/ch63/login

GET : /web-serveur/ch63/admin

Get an access to the admin endpoint.
## Hints 
Source code access
## Solution
As mentioned in the description, I checked the /login path with POST method

![image](https://github.com/user-attachments/assets/188a3c75-2727-4f2e-800a-ca3ae4254368)

The challenge server expects the login and password to be submitted as JSON data in the request body, so I modified the request accordingly:

![image](https://github.com/user-attachments/assets/18ddcf0b-8eb7-401f-96e4-91dabfd3eea9)

The sever returned a JWT token, next I checked the /admin path with GET method

![image](https://github.com/user-attachments/assets/81b26f8c-d58b-4eaa-9e56-e64c23c2122c)

Guess I have to put the JWT in the request, JWTs are often used in a header like this:
`Authorization: Bearer eyJ0eXAiOiJKV1QiLCJh...`

![image](https://github.com/user-attachments/assets/9a0adef3-8421-43b1-9095-cd5d42fce183)

Now, it was time to check the source code.

![image](https://github.com/user-attachments/assets/9a45fafb-f213-45b6-8b5f-2c1bb5a729bf)
![image](https://github.com/user-attachments/assets/5ecb0619-87cf-4509-bc40-76a00182f384)

It seems like the web delete the used JWT after 3 minutes, that doesn't help much attually

![image](https://github.com/user-attachments/assets/45c6bdcd-9256-4cbf-8710-bdef2fb936c6)

The server generates a JWT token from the correct JSON data and then adds it to the blacklist. However, if we could obtain a JWT that isn't on the blacklist, we would get the flag.

Modifing the JWT based on the base64 characteristic, adding '=' in the last of the JWT bypass the blacklist

![image](https://github.com/user-attachments/assets/294baff0-55ec-448f-94d5-625ddd21bce7)

