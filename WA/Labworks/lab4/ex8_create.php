<?php
$servername = "localhost";
$username = "root";
$password = "password";

// Create connection
$conn =  mysqli_connect($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . mysql_connect_error() . "\n");
}
else echo "MySQL conneted successfully\n";


// Create database
$sql = "CREATE DATABASE StudentManagement";

// Check database
if ($conn->query($sql) === TRUE) {
  echo "Database created successfully\n";
} else {
  echo "Error creating database: " . $conn->error . "\n";
}
?>