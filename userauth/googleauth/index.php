<?php 
require_once 'app/init.php';
$googleClient = new Google_Client;
$auth = new GoogleAuth($googleClient);