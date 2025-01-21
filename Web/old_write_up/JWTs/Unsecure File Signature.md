## Description
(K)ind (I)dentification (D)ance## Hints 

A previous Root Me administrator is trying to replicate the website after being banned for sharing challenge solutions. Try to find out if he is hiding any other flags on his new website.
## Solution
Open the challenge and we have access to a JWT

![image](https://github.com/user-attachments/assets/3c47b9e3-ec19-4b7b-a392-0db922781911)

Arcording to the hint of the challenge, I changed the kid value to `../../../../dev/null` and user to `admin`

![image](https://github.com/user-attachments/assets/5e89505a-288b-4aaa-8d62-2e6b698174a6)

Then i tried to changed the kid value to `....//` and the web return `../`, means that it filter out the `../`. So I used the payload: `....//....//....//....//dev/null`

![image](https://github.com/user-attachments/assets/dce8ec42-dae4-4b02-b51e-2d41cd44dd9c)

Now we need to modify the signature so it is coherent with the key file. Fortunately we know the content of dev/null: null.
For that we start by creating a key. In burp in the JWT Editor Keys tab we create a New Symmetric Key. We click on Generate.
The trick is then to change the k of the key to AA== which is the base64 encoded Null Byte.

![image](https://github.com/user-attachments/assets/bcff0077-215a-4cd1-8810-6f5aeb95b3f5)
Back in our repeater tab we click on Sign and chose the previously created key.

![image](https://github.com/user-attachments/assets/7d19595c-16ec-46b9-9f0f-792786a04791)
We send the request to get the flag.
