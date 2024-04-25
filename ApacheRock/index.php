<html>
<body>

<?php
$hostname = getenv('DBSERVER', true) ?: getenv('DBSERVER');
$username = getenv('DBUSER', true)   ?: getenv('DBUSER');
$password = getenv('DBPASS', true)   ?: getenv('DBPASS');
$database = getenv('DBNAME', true)   ?: getenv('DBNAME');

$con = @mysqli_connect($hostname, $username, $password, $database);

if (!$con) {
	echo "Error: " . mysqli_connect_error();
	exit();
}

echo "<h3>All rock discs</h3>\n";

$sql    = "SELECT id, title, year, genre FROM discs;";
$result = mysqli_query($con, $sql);

while ($row = mysqli_fetch_array($result))
{
        echo "Title: ". $row["title"]. "<br />\n";
}

mysqli_close($con);
?> 

</body>
</html>
