<html>
<head>
	<title>Table</title>
	<style>
		th {
			padding: 0px 100px 0px 100px;
		}
	</style>
</head>
<body>
<?php
$info = array( array("Firstname"=>"Jill", "Lastname"=>"Smith" , "Age"=>50),
			   array("Firstname"=>"Eve", "Lastname"=>"Jackson" , "Age"=>94),
			   array("Firstname"=>"John", "Lastname"=>"Doe" , "Age"=>80)
             ); 
?>
<?php if (count($info) > 0): ?>
<table border="1">
  <thead>
    <tr>
      <th><?php echo implode('</th><th>', array_keys(current($info))); ?></th>
    </tr>
  </thead>
  <tbody>
<?php foreach ($info as $row): array_map('htmlentities', $row); ?>
    <tr>
      <td><?php echo implode('</td><td>', $row); ?></td>
    </tr>
<?php endforeach; ?>
  </tbody>
</table>
<?php endif; ?>
</body>
</html>
