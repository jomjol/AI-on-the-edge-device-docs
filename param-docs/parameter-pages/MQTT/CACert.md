# Parameter `CACert`
Default Value: `""`

Example: `/config/certs/RootCA.pem`.

!!! Warning
    This is an **Expert Parameter**! Only change it if you understand what it does!

Path to the CA certificate file.

!!! Note
    This also means that you might have to change the protocol and port in [uri](https://jomjol.github.io/AI-on-the-edge-device-docs/Parameters/#parameter-uri) to `mqtts://IP-ADRESS:8883`!
