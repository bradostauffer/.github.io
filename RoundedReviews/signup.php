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
		$result = $conn->query("SELECT * FROM 
			users where Username='$name';");
                if ($result->num_rows == 0) {
			$_SESSION['login_user'] = $name;
			$conn->query("INSERT INTO users VALUES
				((id),'$name','$pass')");
                        header('Location: /rr.php');       
                } else {
			$ename = "Username already taken";     
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


