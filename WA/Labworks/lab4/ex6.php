<!DOCTYPE html>
<html>  
<head>  
<title>Sort array</title>  
</head>  
<body>  
<form method="post">  
    Enter the Array:<br>  
    <input type="text" name="input">  
    <input type="submit" name="submit" value="Submit">  
</form>  
<?php   
    if($_POST) {
        //getting value from input text box 'input'  
        $input = $_POST['input'];
        if (empty($input)) {
        	echo "No number entered";
        }
        else {
            $arr = explode(",", $input);
            sort($arr);
            echo "Sorted array is: ";
            for ($i = 0; $i < count($arr); $i++) {
                if ($i == count($arr) - 1) echo $arr[$i];
                else echo $arr[$i] . ", ";
            }
        }
    }
?>
</body>  
</html>  