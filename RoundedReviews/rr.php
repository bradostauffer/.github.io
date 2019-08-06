<!DOCTYPE html>
<html>
<?php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
include 'session.php';

?>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<head>
	<title>Rounded Reviews</title>

	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
	<script>
		function showbar(){
			var x = document.getElementById("searchbar");
  			if (x.style.display === "block") {
    			x.style.display = "none";
  			} else {
   				x.style.display = "block";
  			}
		}		

		function signedin() {
				document.getElementById("signin").href = 
					"/logout.php";
		}	
	</script>


	<style>
		*{
			box-sizing: border-box;
		}

  	.container {
 	 	position: absolute;
  		right: 50%;
  		background-color: white;
}

		input[type=text]{
			 background-color: white;
			 background-position: 10px 10px;
			 margin-top: 10%;
			 margin-left: 30%;
			 padding:10px 250px 10px 0px;
			 font-size: 15px;

		}
		input[type=text]:focus{
			border: 3px solid #555;
		}
		.container-top{  
			display: inline-block;
			width:100%;
			height: 55%;
			

		}
		a.header {
			width:100%;
			font-size: 40px;
			letter-spacing: 4px;
			text-align: center;
			text-decoration: none;
			font-family: "Courier New";
			font-weight: bold;
			color:red;

		}
		#caption {
			float: right;
			font-size: 20px;
			letter-spacing: 3px;
			color: black;
		}

	.navbar{
		list-style-type: none;
		margin: 0;
		padding:0;
		overflow: hidden;
		background-color: black;
		width: 100%;
		max-width: 100%; 
		

	}
	li {
		float: left;
	}
	li a {
		display: block;
		color: white;
		text-align: center;
		font-family: "Courier New";
		padding: 20px 25px;
		text-decoration: none;

	}
	li a:hover {
		background-color: red;
	}
	#searchbar {
		display: none;
	}
	.droppingdown{
		float:left;
		overflow: hidden;
	}
	.droppingdown .dropbtn  {
		color: white;
		border:none;
		outline: none;
		font-family: inherit;
		background-color: inherit;
		padding: 20px 25px;
		

	}
	
	.dropcontent{
		display: none;
		position: absolute;
		background-color: grey;
		min-width: 160px;
		box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
	}
	.dropcontent a {
		color: black;
		padding: 10px 6px 6px 10px;
		text-decoration: none;
		display: block;
	}
	.dropcontent a:hover {
		background-color: red;
	}

	.droppingdown:hover .dropcontent {
		display: block;

	}

	</style>
</head>
<body id="home">
<div class="container-top">
	<span>
		<a class="header" href="RoundedReviews.com">
			RoundedReviews.com
		</a>
		<i style="font-size: 39px;" class="fas fa-pizza-slice"></i>
		<p id="caption">
			The source for all your dining debacles
		</p>
	</span>
</div>

	<div class="navbar">
		<div class="droppingdown">
			<button class="dropbtn" href="#home"><i style="font-size: 16px;" class="fas fa-bars"></i></button>
			<div class="dropcontent">
				<a href="#">Link 1 </a>
				<a href="#">Link 2</a>
				<a href="#">Link 3</a>
			</div>
		</div>
		<li><a title="Top 10 Restaurants Near You" href="#">Top 10</a></li>
		<li><a title="Find Restaurants" onclick="showbar()" href="#home">Search</a></li>
		<li style="float:right";><a id="signin" href="/logout.php">Sign Out</a></li>
	</div>

 <div id="searchbar">
	<form>
		<input type="text" name="restaurant" placeholder="Find Restaurants Near You">
		<input type="submit" name="Submit">
	</form>
</div>

</body>
</html>
