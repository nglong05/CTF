### websites i'd never read but anyway:
https://book.hacktricks.xyz/

https://tools.ietf.org/html/rfc2616

https://developer.mozilla.org/en-US/docs/Web

## WebDecode
the very first web exploitation problem, the hints are using a "web inspector" and the flag may be decoded

![Screenshot 2024-07-21 002225](https://github.com/user-attachments/assets/9ddb487a-9cd0-4b38-ae9a-3e8edfa29c9a)
sure enough, using burpsuite we would get the flag easily
## Unminify
the idea is using unminify to get the flag

![Screenshot 2024-07-21 002630](https://github.com/user-attachments/assets/9860890a-93ea-43dc-8ac2-39847440134d)
## More SQLi
a basic sql injection, setting the password to ' or 1=1;-- solve the challenge because it'd be password = '' AND username = '' or 1=1;--'

![Screenshot 2024-07-21 003358](https://github.com/user-attachments/assets/2a90d81c-9961-4446-b50a-a585f436fd6e)
## findme
the hint is "any redirections?", something must be in the networking, using burpsuite we get the flag divided by 2 parts

![Screenshot 2024-07-21 004125](https://github.com/user-attachments/assets/6c50c2b1-a609-449f-bd6a-3415daac9fa0)
![Screenshot 2024-07-21 004134](https://github.com/user-attachments/assets/6a541abb-469a-4e38-be95-4f50f8c051bb)
## Secrets
check the source code we see a link, and since the hint is "folders", playing around with the url solve the problem

![Screenshot 2024-07-21 013144](https://github.com/user-attachments/assets/a4caf3e6-253d-489c-bbb3-bb061bceded1)
![Screenshot 2024-07-21 013359](https://github.com/user-attachments/assets/16326a83-182d-467c-a079-41c1946d57a8)
## Search source
a really sad challenge, just remember to search the whole source code first

![Screenshot 2024-07-21 015939](https://github.com/user-attachments/assets/cd293c8a-575b-4fbe-871a-065131b61752)
## Roboto Sans
check the /robots.txt and get the hint, change the url

![Screenshot 2024-07-21 021143](https://github.com/user-attachments/assets/afc6d47a-8cc3-49c3-b9df-13651578d10b)
## JAuth
a JSON Web Token related problem which can be solved by using "none attack", change the jwt's alg to "none" and user to "admin", delete the signature part and send it back to the sever

i spent 3 fucking hours on this because i missed the dot "." in the last of the payload

![Screenshot 2024-07-21 133257](https://github.com/user-attachments/assets/a2eef32e-a544-45a4-b586-4da446e444b6)
some very cool websites about JWT:

https://viblo.asia/p/json-web-token-hay-session-cookies-dau-moi-la-chan-ai-Qbq5Q0oJlD8

https://medium.com/@musab_alharany/10-ways-to-exploit-json-web-token-jwt-ac5f4efbc41b

https://token.dev/
## caas
use command injection we get the flag 

![Screenshot 2024-07-21 140549](https://github.com/user-attachments/assets/dc2a5770-5920-48c5-9155-2dcb28f1c318)
## Scavenger Hunt
we find in the source code part 1 and 2 of the flag, open /robots.txt file give us part 3 of the flag

![Screenshot 2024-07-22 123847](https://github.com/user-attachments/assets/34485211-61ce-4a7e-bb50-dac5eb3add1c)
it's a apache sever and we should "access" the flag, after quite a time searching google i found that apache sever have a .htaccess file
        
an .htaccess file is used for an Apache web server as a way to configure the details of your website without altering the server configuration files. this file begins with a period to signify that it’s hidden within the folder

![Screenshot 2024-07-22 123856](https://github.com/user-attachments/assets/aad5fd6e-f065-41a6-9a73-e2eefd76f8f1)
due to the hint of using "mac" and "store", we check the .DS_Store file and got the final part of the flag

![Screenshot 2024-07-22 123905](https://github.com/user-attachments/assets/dc6381ae-4dee-45c5-bd44-211167da58ba)
## Who are you?
the first hint is "people using PicoBrowser", i tried to add Referer to the original website but it didn't work, then i try to change agent-user to PicoBrowser, it did work.

![Screenshot 2024-07-22 130937](https://github.com/user-attachments/assets/15966851-2413-4a07-bde8-7f3898c7a6f2)
this time it must be changing the Referer, change it to the first url

![Screenshot 2024-07-22 130949](https://github.com/user-attachments/assets/4ded3f36-ae77-4ee9-b6f5-bde3dd7eb8d5)
change the date to 2018, [how to change the date](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Date)

![Screenshot 2024-07-22 131010](https://github.com/user-attachments/assets/7163c237-7b0f-4a11-b868-acbb21f69d27)
The DNT (Do Not Track) request header indicates the user's tracking preference. It lets users indicate whether they would prefer privacy rather than personalized content.

add "DNT: 1" led us to the next page

![Screenshot 2024-07-22 131145](https://github.com/user-attachments/assets/ceb45488-d23e-42ca-a1b8-e39e739ed0f2)
one way to change the IP address is to add "X-Forwarded-For" with the IP address, find a sweden ip address and proccess

![Screenshot 2024-07-22 131406](https://github.com/user-attachments/assets/24de3c14-9323-4f2b-b9be-965b9cb71f68)
"Accept-Language: sv-SE" and we solve the challenge

![Screenshot 2024-07-22 133915](https://github.com/user-attachments/assets/86d62b7e-c9e9-4f7f-8513-66df73340cbe)

![Screenshot 2024-07-22 133933](https://github.com/user-attachments/assets/fe254bd1-1072-403b-8f59-10a118d885e9)































