<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "database";

$newStatus = $_POST['status'];

$response = array();

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Veritabanı hatası: " . $conn->connect_error);
}

$sql = "UPDATE control SET status='$newStatus' WHERE control_id=1"; 
if ($conn->query($sql) === TRUE) {
    $response['message'] = "PING GONDERILDI";
} else {
    $response['message'] = "HATA: " . $conn->error;
}

$conn->close();

echo json_encode($response);
?>
