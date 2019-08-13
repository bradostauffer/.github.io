<!DOCTYPE html>
<html>
<?php
//ini_set('display_errors', 1);
//ini_set('display_startup_errors', 1);
//error_reporting(E_ALL);
include ('session.php');
include ('result_process.php');

?>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<head>
	<title>Rounded Reviews</title>

	<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
	<link rel="stylesheet" type="text/css" href="/r.css">
	<script>
		function showbar(){
			var x = document.getElementById("searchbar");
  			if (x.style.display == "block") {
    			x.style.display = "none";
  			} else {
   				x.style.display = "block";
  			}
		}		

		function signedin() {
				document.getElementById("signin").href = 
					"/logout.php";
		}
		function res() {
			var r = document.getElementById("r");
			var s = document.getElementById("s");
			var t = document.getElementById("t");
			r.style.display="block";
			s.style.display="block";
			t.style.display="block";
			
			}
		
	</script>

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
	<form action = "" method="get">
	     <span><input type="text" name="restaurant" 
		placeholder="restaurant name"></span>
	     <span><input type="text" name="location" placeholder="what city is it located in"></span>
	     <input type="submit" name="submit">
	</form>
</div> 
<div>
<p style="color:darkred; text-align:center; font-size:27px;
font-family:'Courier New';font-weight:bold"> <?php echo ($restaurant); ?> </p>
<p class="restaurant"> <?php echo "Google: $googlereview out of 5 stars";  ?></p>
<p class="restaurant"> <?php echo "Yelp: $yelpreview out of 5 stars";  ?></p>
<p class="restaurant"> <?php echo "Average Rating: $avg out of 5 stars";  ?></p>

</div>
</body>
</html>
