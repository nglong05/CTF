## Description
No description
## Hints 
- Try creating a new page
- How are pages indexed?
## Solution
This is the website of the challenge:

![Screenshot 2024-07-26 011051](https://github.com/user-attachments/assets/13015a04-5e5c-4a3d-a1f4-db4ea21b6fc8)

The website gives us 3 links with the following pages:

![Screenshot 2024-07-26 011103](https://github.com/user-attachments/assets/77395c4a-a1ce-44a3-9c78-ac68cbe6e91d)

![Screenshot 2024-07-26 011109](https://github.com/user-attachments/assets/6c9bd9a5-cfa8-43d6-8365-354b57b1887f)

![Screenshot 2024-07-26 011114](https://github.com/user-attachments/assets/c78ae3f5-c7fe-4f3c-8189-62cca1f95b97)

Take a look at the `Create Page` page. If we create a new page, it makes the new page's url to **/page/13**, but there are just 2 pre-created page with the url **/page/1** and **/page/2**, so there might be something between them. I tried every link from **/page/3** to **/page/12** and get the 404 error.

![Screenshot 2024-07-26 011151](https://github.com/user-attachments/assets/c0fec301-ee15-4d7d-b419-da916cce2024)

Except for the /page/6, the website give 403 error.

This is a common vulnerability called [Insecure Direct Object Reference](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html), aka IDOR.

Every page has its own edit page, so I tried the **/page/edit/6** url, we got the first flag.

![Screenshot 2024-07-26 011338](https://github.com/user-attachments/assets/fe95ca24-7b54-4295-8d6c-6eaedbfe03b6)

There's one more thing with the `Create Page`, when I create a new page, the details of the new page are reflected in the response, so the website might be vulnerable to XSS (Cross-site scripting). 

- [Basic cover about XSS](https://viblo.asia/p/ky-thuat-tan-cong-xss-va-cach-ngan-chan-YWOZr0Py5Q0).
- https://portswigger.net/web-security/cross-site-scripting

I first used XSS with the body, but it didn't work. Luckily, the title input isn't sanitized. I changed the title with the payload: `<script>alert('hello')</script>`, and we got the second flag when we went back to the home page.

![Screenshot 2024-07-26 011536](https://github.com/user-attachments/assets/a086dbd1-fa8d-402b-8c4d-dd1c356ba332)

The pre-created pages give us a hint of using JavaScript injection (there's a button), so i added `onclick="alert(hello)"` to the button of the page, since <script> is filtered but not attributed inside <>, the third flag is in the source code.

![Screenshot 2024-07-26 012005](https://github.com/user-attachments/assets/c3805d7b-b7ae-46f6-bd0d-4998862b4bc6)

Another common injection is SQLi, so I changed the URL of the page and got the final flag.

![Screenshot 2024-07-26 012224](https://github.com/user-attachments/assets/b83a3687-e71c-405d-935b-8461bec3e16f)

I want to give my thanks to `Bernardo de Araujo`, `ternera`, `anushang` and `isaac wangethi` for their write-ups, i had no idea what to do before reading them.
