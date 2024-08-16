## Description
Check the admin scratchpad! https://jupiter.challenges.picoctf.org/problem/63090/ or http://jupiter.challenges.picoctf.org:63090
## Hints 
- What is that cookie?
- Have you heard of JWT?
## Solution
Upon opening the challenge website, we find a login interface that accepts any username, except for "admin."

![Screenshot 2024-08-16 110511](https://github.com/user-attachments/assets/09d926b3-e9c4-4149-adbb-464a185245fb)

If we modify the JWT's user field to "admin," the page returns an error, indicating that the challenge isn't that straightforward.

I also tried "none" algorithm attack but it didn't work.

The page might be hinting at another approach, is to using [JohnTheRipper](https://www.openwall.com/john/doc/FAQ.shtml) tool to crack the signature part of the jwt. I created a file named jwt.txt to store the JWT and used JohnTheRipper to brute-force the signature. 

The command I used was:  `john --format=HMAC-SHA256 --wordlist=/home/nguyenlong05/bforce/rockyou.txt jwt.txt` 

![Screenshot 2024-08-16 111536](https://github.com/user-attachments/assets/2addf6ab-a442-4a07-abf3-da73c819c698)

After modifying the JWT, we successfully obtained the flag.

![Screenshot 2024-08-16 111707](https://github.com/user-attachments/assets/891e56a6-3dfb-4fee-8d6c-01dfc77063bc)
