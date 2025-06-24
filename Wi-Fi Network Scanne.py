#For Linux
import subprocess

def scan_wifi():
    result = subprocess.check_output(["nmcli", "-t", "-f", "SSID,SIGNAL", "dev", "wifi"])
    print("Available Networks:\n")
    print(result.decode())

scan_wifi()

#For windowds
import subprocess

def scan_wifi_windows():
    try:
        result = subprocess.check_output(["netsh", "wlan", "show", "networks", "mode=bssid"], shell=True)
        print(result.decode(errors="ignore"))
    except subprocess.CalledProcessError as e:
        print("Error scanning Wi-Fi networks:", e)

scan_wifi_windows()
