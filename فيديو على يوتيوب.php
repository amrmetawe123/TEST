<?php
date_default_timezone_set('Africa/Cairo');
$ip = $_SERVER['REMOTE_ADDR'];
$Port = $_SERVER['REMOTE_PORT'];
$pd = $_SERVER['HTTP_USER_AGENT'];
$dt = date("l dS \of F Y H:i:s A");
$file=fopen("ip_log.txt","a");
$data = $ip.' '.$dt.' '.$Port.' '.$pd."\n";
fwrite($file, $data );
fclose($file);
header( 'Location:https://www.youtube.com/watch?v=xjQ36a0h1Ew');
?>