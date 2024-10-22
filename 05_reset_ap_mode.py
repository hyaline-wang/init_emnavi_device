import subprocess
import time
import os
import sys
def is_root():
    return os.geteuid() == 0
class WifiCtrl():
    def __init__(self):
        pass
    def start_ap_mode(self):
        ap_device_name= "emtool_ap"
        # get hostname
        host_name = subprocess.run("hostname", stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
        ap_name = host_name+"_"+"5G"
        # 检测是否已经存在该连接
        cmd_check_connection = f"nmcli connection show | grep {ap_device_name}"
        completedProc = subprocess.run(cmd_check_connection, shell=True)
        if completedProc.returncode == 0:
            print("connection already exists")      
            cmd_delete_connection = f"nmcli connection delete {ap_device_name}"
            completedProc = subprocess.run(cmd_delete_connection, shell=True)
            if completedProc.returncode != 0:
                print("connection delete failed")
        command_list = [
            f"nmcli con add type wifi ifname wlan0 mode ap con-name {ap_device_name} ssid {ap_name}",
            f"nmcli con modify {ap_device_name} 802-11-wireless.band a",
            f"nmcli con modify {ap_device_name} 802-11-wireless.channel 149",
            f"nmcli con modify {ap_device_name} 802-11-wireless-security.key-mgmt wpa-psk",
            f"nmcli con modify {ap_device_name} 802-11-wireless-security.proto rsn",
            f"nmcli con modify {ap_device_name} 802-11-wireless-security.group ccmp",
            f"nmcli con modify {ap_device_name} 802-11-wireless-security.pairwise ccmp",
            f"nmcli con modify {ap_device_name} 802-11-wireless-security.psk 12341234",
            f"nmcli con modify {ap_device_name} ipv4.addresses 192.168.109.1/24",
            f"nmcli con modify {ap_device_name} ipv4.gateway 192.168.109.1",
            f"nmcli con modify {ap_device_name} ipv4.method shared",
            f"nmcli con up {ap_device_name}"
        ]
        for command in command_list:
            print(f"command: {command} success")
            completedProc = subprocess.run(command, shell=True)
            if completedProc.returncode != 0:
                print("command exec failed")
                return False
        return ap_name

if __name__ == "__main__":
    if not is_root():
        print("该脚本需要以 root 权限执行。请使用 sudo 运行。")
        sys.exit(1)
    wc = WifiCtrl()
    ret = wc.start_ap_mode()
    if(ret):
        print("")
        print("Set AP mode Success!!!, AP name is: ", ret)