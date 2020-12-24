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

$sql = "UPDATE info SET class='Two' WHERE mark < 60";

if ($conn->query($sql) === TRUE) {
  echo "Record updated successfully";
} else {
  echo "Error updating record: " . $conn->error;
}
?>