## Description
I found a web app that can help process images: PNG images only!
## Hints 
None
## Solution
This is the website of the challenge:

![Screenshot 2024-08-14 223902](https://github.com/user-attachments/assets/34d113f0-868f-45bd-b493-b974236d056d)

Checking the page `/robots.txt` lead us to the page `/instructions.txt`

![Screenshot 2024-08-14 224013](https://github.com/user-attachments/assets/b3101223-4d19-444a-8296-f170183b90d0)

![Screenshot 2024-08-14 224118](https://github.com/user-attachments/assets/234dac5a-8788-4b63-baac-599dca37b141)

We could try to make a php cmd payload to the sever and see how the web app responds.

![Screenshot 2024-08-14 233912](https://github.com/user-attachments/assets/ff5bee03-e112-43ac-a55d-776a43301d00)

The file is not a valid PNG image, arcoding to the instruction page I changed the first few byte 'magic bytes' for the PNG format, for example:

![Screenshot 2024-08-14 234632](https://github.com/user-attachments/assets/fa838c4f-a739-4cff-bb5b-8b89a3239f1a)

Adding PNG to the first part of the file.......
