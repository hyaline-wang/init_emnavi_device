# init_emnavi_device

使用
```bash
# 为设备设置默认密码 emNavi
sudo bash ./00_reset_default_root_passwd.sh

# 更新设备 hostname
sudo python ./01_rename_hostname.py

# 重命名用户名 【可选】
sudo bash ./02_rename_username.sh <old_username> <new_username>

# 为用户重设密码
sudo bash ./03_reset_default_passwd.sh <username>

# 清除所有保存的wifi连接
sudo python3 ./04_clean_wifi_connect.py

# 将设备设置成 AP 模式
sudo python3 ./05_reset_ap_mode.py
```