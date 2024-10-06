#!/bin/bash

# 检查是否提供了用户名参数
if [ -z "$1" ]; then
    echo "请提供用户名"
    exit 1
fi

USERNAME=$1
NEW_PASSWORD="123456"

# 重置用户密码为123456
echo "$USERNAME:$NEW_PASSWORD" | chpasswd

# 检查是否成功
if [ $? -eq 0 ]; then
    echo "用户 '$USERNAME' 的密码已重置为 '123456'."
else
    echo "重置密码失败"
    exit 1
fi
