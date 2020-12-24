<!DOCTYPE html>
<html>  
<head>  
<title>Factorial</title>  
</head>  
<body>  
<form method="post">  
    Enter the Number:<br>  
    <input type="number" name="number">  
    <input type="submit" name="submit" value="Submit">  
</form>  
<?php   
    if($_POST) {  
        $fact = 1;  
        //getting value from input text box 'number'  
        $number = $_POST['number'];
        if (empty($number)) {
        	echo "No number entered";
        }
        else {
        	echo "Factorial of $number:<br>";  
	        //start loop  
	        for ($i = 1; $i <= $number; $i++) {         
	            $fact = $fact * $i;  
	        }  
	        echo $fact . "<br>";  
        }
        
    }
?>
</body>  
</html>  