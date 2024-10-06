#!/bin/bash
# 检查是否是 root 用户
if [ "$EUID" -ne 0 ]; then
  echo "Error: This script must be run as root."
  exit 1
fi

# 检查是否提供了足够的参数
if [ $# -ne 2 ]; then
  echo "Usage: $0 old_username new_username"
  exit 1
fi

OLD_USERNAME=$1
NEW_USERNAME=$2

# 检查 old_username 是否存在于 /etc/passwd 中
if ! grep -q "^$OLD_USERNAME:" /etc/passwd; then
  echo "Error: User '$OLD_USERNAME' does not exist."
  exit 1
fi

# 检查主目录是否存在
if [ ! -d "/home/$OLD_USERNAME" ]; then
  echo "Error: Home directory for user '$OLD_USERNAME' does not exist."
  exit 1
fi

# 检查新用户名的主目录是否已存在，避免冲突
if [ -d "/home/$NEW_USERNAME" ]; then
  echo "Error: Home directory for new username '$NEW_USERNAME' already exists."
  exit 1
fi

# 备份原文件
echo "Backing up system files..."
cp /etc/passwd /etc/passwd.bak
cp /etc/shadow /etc/shadow.bak
cp /etc/group /etc/group.bak

# 替换用户名
echo "Replacing $OLD_USERNAME with $NEW_USERNAME in system files..."
sed -i "s/$OLD_USERNAME/$NEW_USERNAME/g" /etc/passwd
sed -i "s/$OLD_USERNAME/$NEW_USERNAME/g" /etc/shadow
sed -i "s/$OLD_USERNAME/$NEW_USERNAME/g" /etc/group

# 重命名用户的主目录
echo "Renaming home directory from /home/$OLD_USERNAME to /home/$NEW_USERNAME..."
mv /home/$OLD_USERNAME /home/$NEW_USERNAME

# 修改用户主目录的权限，确保新用户拥有正确的权限
echo "Updating ownership for the new home directory..."
chown -R $NEW_USERNAME:$NEW_USERNAME /home/$NEW_USERNAME

echo "Username and home directory replacement completed."

# 提示重启
echo "Please reboot the system to apply the changes: sudo reboot"
