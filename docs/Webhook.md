# Webhook

Comming soon.
See [https://github.com/jomjol/AI-on-the-edge-device/pull/3163](https://github.com/jomjol/AI-on-the-edge-device/pull/3163) and [https://github.com/jomjol/AI-on-the-edge-device/pull/3174](https://github.com/jomjol/AI-on-the-edge-device/pull/3174)

@RaHehl Please add some explanations.
Also I think it would be great to add the PHP examples:
```PHP
<?php
$expectedApiKey = 'testtest2';

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
