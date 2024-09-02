## Description
Congratulations Berthier, thanks to your help the computer has been identified. You have requested a memory dump but before starting your analysis you wanted to take a look at the antivirus’ logs. Unfortunately, you forgot to write down the workstation’s hostname. But since you have its memory dump you should be able to get it back!
## Hints 
The validation flag is the workstation’s hostname.

The uncompressed memory dump md5 hash is e3a902d4d44e0f7bd9cb29865e0a15de
## Solution
- volatility -f ./ch2.dmp imageinfo
- volatility -f ./ch2.dmp --profile=Win7SP0x86 envars
