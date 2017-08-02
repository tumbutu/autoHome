<!doctype html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<title>Auto Home | Aaron</title>
	<link rel="stylesheet" href="site_css.css">
</head>

<body>
	
	<div id="form_div">
	<h2>Home Automation | Aaron</h2>
	<form action="" method="get">
		<button class="button buttonOff" type=submit name="code" value=0>Light off</button> <br/>
		<button class="button buttonOn" type=submit name="code" value=1>Light on</button> <br/>
		<button class="button buttonOff" type=submit name="code" value=0>Fan off</button> <br/>
		<button class="button buttonOn" type=submit name="code" value=1>Fan on</button> <br/>
	</form>
	</div>
	<?php 
		if(isset($_GET["code"])){
			$code = $_GET["code"];
			#exec("python /home/pi/Desktop/src/gh/blink_led");
			#$result = json_decode(exec("python /home/pi/Desktop/src/gh/test.py"),true);
			#echo $result["on"];
			$fp = fopen('/home/pi/Desktop/src/gh/switch.txt','w');
			fwrite($fp, $code);
			fclose($fp);
		}
	
	?>

</body>
</html>
