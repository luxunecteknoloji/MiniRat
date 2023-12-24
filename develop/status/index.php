<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Status</title>
</head>
<body>
    <div>
        <div id="status">
            <?php echo getStatusFromDatabase(); ?>
        </div>
    </div>
</body>
</html>

<?php
function getStatusFromDatabase() {
    
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "rit";

    $conn = new mysqli($servername, $username, $password, $dbname);

    if ($conn->connect_error) {
        die("MySQL Connection failed: " . $conn->connect_error);
    }

    // Kontrol tablosundan durumu al
    $sql = "SELECT status FROM control WHERE control_id=1"; // Sadece "control_id" sütununu kullan
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Durumu ekrana yazdır
        $row = $result->fetch_assoc();
        $status = $row["status"];
        return "Status: " . $status;
    } else {
        return "No data found";
    }

    // MySQL bağlantısını kapat
    $conn->close();
}
?>
