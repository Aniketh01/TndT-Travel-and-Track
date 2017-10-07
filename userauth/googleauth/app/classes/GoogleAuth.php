<?php 

class GoogleAuth {
	public function __construct(Google_client $googleClient = null) {
		$this->client = $googleClient;
		if($this->client) {
			$this->client->setScopes('email');
			$this->client = new Google_Client();
			$this->client->setAuthConfig('/home/amrit/Desktop/googleauth/client_secret_1086787438889-otegd06np7c6qrj4iss256n0ronibv7g.apps.googleusercontent.com.json');
			$redirect_uri = 'http://' . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'];
			$this->client->setRedirectUri($redirect_uri);



		}
	}
}
