## Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
## Hints 
What's causing the 'corruption' of the image?
## Solution
This is the image from the challenge:

![Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada flag](https://github.com/user-attachments/assets/7bafa81e-af46-40c0-9a25-9875f26c6f02)

The image appears broken due to an MSB shift. The description indicated that the image passed an LSB test, which makes sense because the image is heavily corrupted. The corruption is likely caused by a shift in the MSB, creating a noticeable visual difference in the picture.

I used `Stegsolve` to modify the bits of the image. By changing the most significant bit (the 8th bit), I was able to reveal some plaintext that contained the flag.
![Screenshot 2024-08-16 170719](https://github.com/user-attachments/assets/211d3172-3110-4ce5-9045-e795d54a1d42)

