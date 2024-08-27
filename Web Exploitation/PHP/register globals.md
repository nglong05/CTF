## Description
none
## Hints 
It seems that the developper often leaves backup files around...
## Solution
After a time playing around with the website, i used dirsearch to find others path of the website.

![image](https://github.com/user-attachments/assets/52ded773-a039-4fb3-a798-8ac95c578a88)
Download the index.php.bak I got the source code. 

Here is the source code of the challenge:
```php
<?php
function auth($password, $hidden_password){
    $res=0;
    if (isset($password) && $password!=""){
        if ( $password == $hidden_password ){
            $res=1;
        }
    }
    $_SESSION["logged"]=$res;
    return $res;
}
```
This function take $password and compare it with a $hidden_password. If the password matches, the function sets a session variable `$_SESSION["logged"] = 1`.
```php

function display($res){
    $aff= '
	  <html>
	  <head>
	  </head>
	  <body>
	    <h1>Authentication v 0.05</h1>
	    <form action="" method="POST">
	      Password&nbsp;<br/>
	      <input type="password" name="password" /><br/><br/>
	      <br/><br/>
	      <input type="submit" value="connect" /><br/><br/>
	    </form>
	    <h3>'.htmlentities($res).'</h3>
	  </body>
	  </html>';
    return $aff;
}
```

```php

session_start();
if ( ! isset($_SESSION["logged"]) )
    $_SESSION["logged"]=0;
```
If the session variable $_SESSION["logged"] is not set, it initializes it to 0
```php
$aff=""; //hold the HTML output
include("config.inc.php");

if (isset($_POST["password"]))
    $password = $_POST["password"];

if (!ini_get('register_globals')) {
    $superglobals = array($_SERVER, $_ENV,$_FILES, $_COOKIE, $_POST, $_GET);
    if (isset($_SESSION)) {
        array_unshift($superglobals, $_SESSION);
    }
    foreach ($superglobals as $superglobal) {
        extract($superglobal, 0 );
    }
}
```
```php
if (( isset ($password) && $password!="" && auth($password,$hidden_password)==1) || (is_array($_SESSION) && $_SESSION["logged"]==1 ) ){
    $aff=display("well done, you can validate with the password : $hidden_password");
} else {
    $aff=display("try again");
}

echo $aff;

?>
```
This block checks if the user has either:
- Entered a valid password `(auth($password, $hidden_password)==1)`.
- Already logged in `($_SESSION["logged"]==1)`.

If either condition is met, the success message is displayed, including the hidden password.

To solve the challenge, I modified the url by adding `?_SESSION[logged]=1`, so that I bypassed the need to enter the correct password.

Or you can first go to this url http://.../ch17/`?password=foo&hidden_password=foo`, so that the session variable logged($_SESSION[’logged’]) is set to 1 in the auth() function. Then, just go again to the challenge without any GET parameters and it will print the password.
