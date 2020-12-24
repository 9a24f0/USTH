<!DOCTYPE html>
<html>  
<head>  
<title>Prime Number</title>  
</head>  
<body>  
<form method="post">  
    Enter the Number:<br>  
    <input type="number" name="number">  
    <input type="submit" name="submit" value="Submit">  
</form>
<?php
    function isPrime($number) {
        for ($i = 2; $i*$i > $number; $i++) {
            if ($number % $i == 0) {
                echo $number . " is not a prime number";
                return;
            }
        }
        echo $number . " is a prime number";
    }
?>
<?php
    if($_POST) {
        //getting value from input text box 'number'  
        $number = $_POST['number'];
        if (empty($number)) {
            echo "No number entered";
        }
        else {
            isPrime($number);
        }
    }
?>
</body>  
</html>  