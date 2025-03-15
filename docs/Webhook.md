# Webhook
## Purpose

The idea behind this webhook feature is to provide an alternative to MQTT and InfluxDB for transmitting data, such as water meter readings from a vacation home, to a standard PHP webspace.

You can call the webhook to upload the data or the raw image of a round to a server.

## Configuration

To configure the webhook feature, you only need to define a URI and an API key. The URI is where the webhook will send the data, and the API key is used to authenticate the requests, ensuring that only authorized devices can send data to your server.
Optionally, "Upload Image" can be used to configure whether an additional PUT request should be sent to the same URI with the current image.
A parameter timestamp is appended to establish a correlation.

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
    "timestamp": "2024-08-09T11:44:44+0200",
    "timestampLong": 1723196684,
    "name": "main",
    "rawValue": "0345.42647",
    "value": "345.42648",
    "preValue": "345.42648",
    "rate": "0.000000",
    "changeAbsolute": "0.00000",
    "error": "no error"
  },
  {
    "timestamp": "2024-08-09T11:44:44+0200",
    "timestampLong": 1723196684,
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

## Basic Example of a server using PHP

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
            $data['timestampLong'], 
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
	$timestamp = $_GET['timestamp'];

    if (!ctype_digit($timestamp) || $timestamp < 0 || $timestamp > PHP_INT_MAX) {
        http_response_code(400); // 400 Bad Request
        echo json_encode(['status' => 'error', 'message' => 'Invalid timestamp']);
        exit;
    }
	
    $imageFilePath = 'uploaded_image_' . $timestamp . '.jpg';

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

## Basic Example of a server using Python
```Python
from flask import Flask, request, jsonify
import csv
import os

app = Flask(__name__)

# List of allowed API keys
ALLOWED_API_KEYS = {
    '123',
    '456',
    '789'
}

@app.before_request
def check_api_key():
    # Get the API key from the request headers
    received_api_key = request.headers.get('APIKEY')
    
    # Check if the received API key is in the allowed list
    if received_api_key not in ALLOWED_API_KEYS:
        return jsonify({'status': 'error', 'message': 'Invalid API key'}), 403
    
    # Attach the API key to the request object for later use
    request.api_key = received_api_key

@app.route('/webhook', methods=['POST', 'PUT'])
def webhook():
    # Create a directory for the API key if it doesn't exist
    api_key_dir = os.path.join('data', request.api_key)
    os.makedirs(api_key_dir, exist_ok=True)

    if request.method == 'POST':
        # Handle POST request: Write data to CSV
        data = request.get_json()
        if not data or not isinstance(data, list):
            return jsonify({'status': 'error', 'message': 'Invalid JSON data'}), 400

        csv_file = os.path.join(api_key_dir, 'webhook_log.csv')
        try:
            with open(csv_file, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for item in data:
                    csv_writer.writerow([
                        item.get('timestampLong'),
                        item.get('name'),
                        item.get('rawValue'),
                        item.get('value'),
                        item.get('preValue'),
                        item.get('rate'),
                        item.get('changeAbsolute'),
                        item.get('error')
                    ])
            return jsonify({'status': 'success', 'message': 'Data written to CSV file'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': 'Unable to open CSV file'}), 500

    elif request.method == 'PUT':
        # Handle PUT request: Save image
        timestamp = request.args.get('timestamp')
        if not timestamp or not timestamp.isdigit() or int(timestamp) < 0:
            return jsonify({'status': 'error', 'message': 'Invalid timestamp'}), 400

        image_data = request.data
        if not image_data:
            return jsonify({'status': 'error', 'message': 'No image data received'}), 400

        image_file_path = os.path.join(api_key_dir, f'{timestamp}.jpg')
        try:
            with open(image_file_path, 'wb') as image_file:
                image_file.write(image_data)
            return jsonify({'status': 'success', 'message': 'Image uploaded successfully'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': 'Unable to save the image'}), 500

    else:
        # Handle unsupported HTTP methods
        return jsonify({'status': 'error', 'message': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
```
