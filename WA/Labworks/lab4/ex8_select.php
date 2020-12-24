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

function toArray($result) {
	$arr = array();
	if (mysqli_num_rows($result) > 0) {
		while ($row = mysqli_fetch_assoc($result)) {
			$arr[] = $row;
		}
	}
	return $arr;
}

// Best student
$sql = "SELECT * FROM info WHERE mark > 75";
$result = $conn->query($sql);
$best = toArray($result);

// Good student
$sql = "SELECT * FROM info WHERE (mark > 60 AND mark <= 75)";
$result = $conn->query($sql);
$good = toArray($result);

// Average student
$sql = "SELECT * FROM info WHERE mark < 60";
$result = $conn->query($sql);
$avg = toArray($result);
?>

<!DOCTYPE html>
<html>
<head>
</head>
<body>
	<h1>Best Students</h1>
<table border="1">
  <thead>
    <tr>
      <th><?php echo implode('</th><th>', array_keys(current($best))); ?></th>
    </tr>
  </thead>
  <tbody>
<?php foreach ($best as $row): array_map('htmlentities', $row); ?>
    <tr>
      <td><?php echo implode('</td><td>', $row); ?></td>
    </tr>
<?php endforeach;?>
  </tbody>
</table>

	<h1>Good Students</h1>
<table border="1">
  <thead>
    <tr>
      <th><?php echo implode('</th><th>', array_keys(current($good))); ?></th>
    </tr>
  </thead>
  <tbody>
<?php foreach ($good as $row): array_map('htmlentities', $row); ?>
    <tr>
      <td><?php echo implode('</td><td>', $row); ?></td>
    </tr>
<?php endforeach;?>
  </tbody>
</table>

	<h1>Average Students</h1>
<table border="1">
  <thead>
    <tr>
      <th><?php echo implode('</th><th>', array_keys(current($avg))); ?></th>
    </tr>
  </thead>
  <tbody>
<?php foreach ($avg as $row): array_map('htmlentities', $row); ?>
    <tr>
      <td><?php echo implode('</td><td>', $row); ?></td>
    </tr>
<?php endforeach;?>
  </tbody>
</table>

</body>
</html>