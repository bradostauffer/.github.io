<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet"type="text/css"href="/signin1.css">
</head>
<body>
<?php include('signup.php'); 
	$_POST = array();
//	header('cache-control: no-cache, no-store, must-revalidate');
?>
<h1 style="text-align:center;"> SIGN UP </h1>

<div class="login-page">
  <div class="form">
    <form class="login-form"target="_self" 
    method="post" action = "<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>"> 
	<span>* <?php echo $ename; ?></span><br> 
	<input type = "text" placeholder="Username" name="name">
      	<span>*<?php echo $epass; ?></span><br> 
	<input type="password" placeholder="Password" name="password">
	<input type = "submit" name="submit" value="Create Account"> 
	<p class="message"><a href="index.php"> Sign in here</a></p>
   </form>
  </div>
</div>
<?php $conn->close(); ?>
</body>
</html>
