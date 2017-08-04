<!DOCTYPE HTML>
<!--
	Stellar by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Home Automation | Aaron</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		
		<style>
		.room_con, .room_con h3
		{
		  font-size: 14px;
		  font-weight: bold;
		  font-family: sans-serif, Arial
		  color: white;
		}
		</style>
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
	</head>
	<body>
					
			<!-- Header -->
			<header id="header" class="alt">

				<div class="room_con">
					<h3>Current Room Condition</h3>
					<?php						
						$lines = file('/home/pi/Desktop/src/gh/humiTemp.txt');
						
						Echo "Humidity: ".$lines[0]."rh<br/>";
						Echo "Temperature: ".$lines[1]."&#8451";
						Echo "<hr>";
						fclose($humi);
					?> 
				</div>

				<form action="" method="post">
					<span><img width=50px height=60px src=images/light_bulb.png /></span><br/>
					<span><button class="button leftButton" type="submit" name="code" value="1">Light on</button></span>
					<span><button class="button rightButton" type="submit" name="code" value="2">Light off</button></span><br/><br/>
					<span><img width=50px height=60px src=images/fan.png /></span><br/>
					<span><button class="button leftButton" type="submit" name="code" value="3">Fan on</button></span>
					<span><button class="button rightButton" type="submit" name="code" value="4">Fan off</button></span><br/>
				</form>		
				
				<p>Aaron IoT Home Automation Application<br />
						email: <a href="nichieaaron@gmail.com">nichieaaron@gmail.com</a>
			</header>

			<?php
				if(isset($_POST["code"])){
					$code = $_POST["code"];
					#exec("python /home/pi/Desktop/src/gh/blink_led");
					#$result = json_decode(exec("python /home/pi/Desktop/src/gh/test.py"),true);
					#echo $result["on"];
					$fp = fopen('/home/pi/Desktop/src/gh/remote_switch.txt','w');
					fwrite($fp, $code);
					fclose($fp);
				}
			?>

	</body>
</html>
