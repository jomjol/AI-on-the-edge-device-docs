# Webhook

Comming soon.

## Purpose

The idea behind this webhook feature is to provide an alternative to MQTT and InfluxDB for transmitting data, such as water meter readings from a vacation home, to a standard PHP MySQL webspace.

## Configuration

To configure the webhook feature, you only need to define a URI and an API key. The URI is where the webhook will send the data, and the API key is used to authenticate the requests, ensuring that only authorized devices can send data to your server.

## Example of a POST Request

Below is an example of the JSON payload that might be sent in a POST request to the webhook:

### Request Headers

```http
APIKEY: your-api-key-here
```

### JSON Payload

```json
[
  {
    "timeUTC": 1723196684,
    "timestamp": "2024-08-09T11:44:44+0200",
    "name": "main",
    "rawValue": "0345.42647",
    "value": "345.42648",
    "preValue": "345.42648",
    "rate": "0.000000",
    "changeAbsolute": "0.00000",
    "error": "no error"
  },
  {
    "timeUTC": 1723196684,
    "timestamp": "2024-08-09T11:44:44+0200",
    "name": "test",
    "rawValue": "34",
    "value": "34",
    "preValue": "34",
    "rate": "0.000000",
    "changeAbsolute": "0",
    "error": "no error"
  }
]
```

## Basic PHP Example


```PHP
<?php
$expectedApiKey = 'your-api-key-here';

$receivedApiKey = isset($_SERVER['HTTP_APIKEY']) ? $_SERVER['HTTP_APIKEY'] : '';

if ($receivedApiKey !== $expectedApiKey) {
    http_response_code(403); // 403 Forbidden
    echo json_encode(['status' => 'error', 'message' => 'Invalid API key']);
    exit;
}

$method = $_SERVER['REQUEST_METHOD'];

if ($method === 'POST') {
    // Handle POST request: Write data to CSV
    $csvFile = 'webhook_log.csv';

    $jsonData = file_get_contents('php://input');

    $dataArray = json_decode($jsonData, true);
    if (!$jsonData || !is_array($dataArray)) {
        http_response_code(400); // 400 Bad Request
        echo json_encode(['status' => 'error', 'message' => 'Invalid JSON data']);
        exit;
    }

    $csvHandle = fopen($csvFile, 'a');
    if ($csvHandle === false) {
        http_response_code(500); // 500 Internal Server Error
        echo json_encode(['status' => 'error', 'message' => 'Unable to open CSV file']);
        exit;
    }

    foreach ($dataArray as $data) {
        $csvRow = [
            $data['timestamp'], 
            $data['name'], 
            $data['rawValue'], 
            $data['value'], 
            $data['preValue'], 
            $data['rate'], 
            $data['changeAbsolute'], 
            $data['error']
        ];
        fputcsv($csvHandle, $csvRow);
    }

    fclose($csvHandle);

    http_response_code(200); // 200 OK
    echo json_encode(['status' => 'success', 'message' => 'Data written to CSV file']);
} elseif ($method === 'PUT') {
    // Handle PUT request: Save image
    $imageFilePath = 'uploaded_image.jpg';

    $imageData = file_get_contents('php://input');

    if (!$imageData) {
        http_response_code(400); // 400 Bad Request
        echo json_encode(['status' => 'error', 'message' => 'No image data received']);
        exit;
    }

    if (file_put_contents($imageFilePath, $imageData) === false) {
        http_response_code(500); // 500 Internal Server Error
        echo json_encode(['status' => 'error', 'message' => 'Unable to save the image']);
        exit;
    }

    http_response_code(200); // 200 OK
    echo json_encode(['status' => 'success', 'message' => 'Image uploaded successfully']);
} else {
    // Handle unsupported HTTP methods
    http_response_code(405); // 405 Method Not Allowed
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
}
?>
```
