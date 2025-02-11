```php
<?php
define("ALPHA", str_split("abcdefghijklmnopqrstuvwxyz0123456789_-"));
ini_set("error_reporting", 0);

include "flag.php"; // $FLAG
$SEEDS = str_split($FLAG, 4);

function session_id_secure($id) {
    global $SEEDS;
    mt_srand(intval(bin2hex($SEEDS[md5($id)[0] % (count($SEEDS))]),16));
    $id = "";
    for($i=0;$i<1000;$i++) {
        $id .= ALPHA[mt_rand(0,count(ALPHA)-1)];
    }
    return $id;
}

if(isset($_POST['username']) && isset($_POST['password'])) {
    session_id(session_id_secure($_POST['username'] . $_POST['password']));
    session_start();
    echo "Thank you for signing up!";
}else {
    echo "Please provide the necessary data!";
}
?>
```