# Password Protection
The Web Interface and the REST API can be protected by a password.

To do so, you have to set the username and password in the `wlan.ini` file on the SD-Card.
Uncomment (remove the leading `;`) and update the two lines with `http_username` and `http_password`:
```
http_username = "myusername"
http_password = "mypassword"
```

!!! Warning
    This is be a WEAK and INSECURE way to protect the Web Interface and the REST API.
    There was no audit nor a security review to check the correct implementation of the protection!
    The password gets transmitted unencrypted (plain text), this means it is very easy to extract it
    for somebody who has access to your WIFI!
    
    USE AT YOUR OWN RISK!
