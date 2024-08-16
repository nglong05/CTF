## Description
Can you handle APKs?
## Hints 
- Did you know you can unzip APK files?
- Now you have the whole host of shell tools for searching these files.
## Solution
The file we received wasn't an APK file, so I changed the file extension and unzipped it.

![Screenshot 2024-08-16 123710](https://github.com/user-attachments/assets/591e0261-a73a-4688-911f-fea99b34340d)

After unzipping the file, I found a large number of directories and files. I used the command `strings * | grep flag` to quickly search through them and discovered a file named **res/color/flag.txtUT**

![Screenshot 2024-08-16 124017](https://github.com/user-attachments/assets/011be752-903d-4aef-8c8f-755ffc93c888)

The file contained an encrypted string, I use [dcode](https://www.dcode.fr/) tool to get the flag.

![Screenshot 2024-08-16 124228](https://github.com/user-attachments/assets/71282791-3e3d-4415-987b-5f7cb4a55dcf)
