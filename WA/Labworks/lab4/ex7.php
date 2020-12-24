<!DOCTYPE html>
<html>  
<head>  
<title>Reverse</title>  
</head>  
<body>  
<form method="post">  
    Enter the string:<br>  
    <input type="text" name="string">  
    <input type="submit" name="submit" value="Submit">  
</form>  
<?php   
    if($_POST) {  
        $fact = 1;  
        //getting value from input text box 'number'  
        $str = $_POST['string'];
        if (empty($str)) {
        	echo "No string entered";
        }
        else {
            echo "The reversed string is: " . strrev($str);
        }
        
    }
?>
</body>  
</html>  