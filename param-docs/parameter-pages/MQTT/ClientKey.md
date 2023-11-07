# Parameter `ClientKey`
Default Value: `""`

Example: `/config/certs/client.pem.key`.

!!! Warning
    This is an **Expert Parameter**! Only change it if you understand what it does!

Path to the Client Key file.

!!! Note
    This also means that you might have to change the protocol and port in [uri](https://jomjol.github.io/AI-on-the-edge-device-docs/Parameters/#parameter-uri) to `mqtts://IP-ADRESS:8883`!