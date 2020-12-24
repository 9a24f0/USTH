<?php
$servername = "localhost";
$username = "root";
$password = "password";
$database = "StudentManagement";

// Create connection
$conn =  mysqli_connect($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . mysql_connect_error() . "\n");
}
else echo "MySQL conneted successfully\n";

// Create table
$sql = "CREATE TABLE info (
	id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(10) NOT NULL,
	class VARCHAR(10) NOT NULL,
	mark INT UNSIGNED,
	sex VARCHAR(10))";

if ($conn->query($sql) === TRUE) {
  echo "Table 'info' created successfully";
} else {
  echo "Error creating table: " . $conn->error;
}

// Insert value to table `info`
$sql = "INSERT INTO info (id, name, class, mark, sex)
VALUES 	(1, 'Jhon Deo', 'Four', 75, 'female'),
	   	(2, 'Max Ruin', 'Three', 85, 'male'),
		(3, 'Arnold', 'Three', 55, 'male'),
		(4, 'Krish Star', 'Four', 60, 'female'),
		(5, 'Jhon Mike', 'Four', 60, 'female'),
		(6, 'Alex John', 'Four', 55, 'male'),
		(7, 'My Jhon Rob', 'Fifth', 78, 'male'),
		(8, 'Asruid', 'Five', 85, 'male'),
		(9, 'Tes Qry', 'Six', 78, 'male'),
		(10, 'Big John', 'Four', 55, 'female')";

// Check insert
if ($conn->query($sql) === TRUE) {
  echo "New record created successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
?>