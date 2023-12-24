<?php
// MySQL bağlantısı için bilgileri güncelleyin
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "rit";

// POST isteğinden durumu al
$newStatus = $_POST['status'];

// Başlangıçta bir $response değişkeni oluşturun
$response = array();

// MySQL bağlantısını oluştur
$conn = new mysqli($servername, $username, $password, $dbname);

// Bağlantıyı kontrol et
if ($conn->connect_error) {
    die("Veritabanı hatası: " . $conn->connect_error);
}

// Kontrol tablosundaki durumu güncelle
$sql = "UPDATE control SET status='$newStatus' WHERE control_id=1"; // Burada "control_id" sütununu kullanın
if ($conn->query($sql) === TRUE) {
    $response['message'] = "PING GONDERILDI";
} else {
    $response['message'] = "HATA: " . $conn->error;
}

// MySQL bağlantısını kapat
$conn->close();

// JSON formatında yanıtı döndür
echo json_encode($response);
?>
