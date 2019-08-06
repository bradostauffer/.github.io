<?php
session_start();
$page = $_SERVER['PHP_SELF'];
$sec = "2";
$servername = "localhost";
$username = "root";
$password = "brado1998";
$database = "rr";
$ename = $epass = "";
$count = 0;
$name = $pass = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
        if (empty($_POST["name"])) {
                $ename = "Name is required!";
        } else {
                $name = testdata($_POST["name"]);
                $count++;
        }
	if (empty($_POST["password"])) {
                $epass = "Password is required!";
        } else {
                $pass = testdata($_POST["password"]);
                $count++;
        }
        if ($count == 2) {  //if count is 2, means two fields are filled
                $conn = new mysqli($servername, $username, 
                        "brado1998", $database);
                if ($conn->connect_error) {
                        die("connection failed " . $conn->connect_error );
 		}
                $result = $conn->query("SELECT * FROM users");
                if (usr_info_exists($result, $name, $pass)) {
			$_SESSION['login_user'] = $name;
                        header('Location: /rr.php');       
                } else {
			$ename = "Username or Password incorrect";     
                }
	}
//mysqli_free_result($conn);
//$conn->close();
}

function testdata ($data){
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
}


function usr_info_exists($result,$name, $pass){
	while($row = $result->fetch_assoc()) {
		if ($row['Username'] == $name && $row['Password'] == $pass){
			return true;
		}
	}
	return false;

}
?>

