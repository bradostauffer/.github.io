<?php
$servername = "localhost";
$username = "root";
$password = "brado1998";
$database = "rr";
$conn = new mysqli($servername, $username, 
"brado1998", $database);
	session_start();
//	$user_check = $_SESSION['login_user'];
	$result = $conn->query("SELECT * FROM users");
	$row = $result->fetch_assoc();
	$login_session = $row['Username'];
	if (empty($login_session)){
		$conn->close();
		header('Location: index.php');
	}

?>
