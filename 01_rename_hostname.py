# 命名规则
import random
import string
import argparse
import os
import sys

def is_root(): 
	return os.geteuid() == 0
# 在生成主机名之后，设置主机名
def set_hostname(hostname):
    os.system(f"sudo hostnamectl set-hostname {hostname}")

# 生成随机后缀
def generate_random_suffix(length=4):
    characters = string.ascii_letters + string.digits  # 包含字母和数字
    suffix = ''.join(random.choice(characters) for _ in range(length))
    return suffix

# 生成主机名
def generate_hostname(prefix, drone_type, px4_sys_id):
    if not prefix:
        prefix = "emnavi"  # 如果没有提供前缀，则使用默认值
    random_suffix = generate_random_suffix()
    hostname = f"{prefix}-{drone_type}-{px4_sys_id}-{random_suffix}"
    return hostname

if __name__ == "__main__": 
	if not is_root(): 
		print("该脚本需要以 root 权限执行。请使用 sudo 运行。") 
		sys.exit(1)

    # 设置命令行参数解析
    parser = argparse.ArgumentParser(description="生成无人机主机名")
    parser.add_argument("--prefix", type=str, help="前缀(默认为 'emnavi')")
    parser.add_argument("--drone_type", type=str, required=True, help="无人机类型")
    parser.add_argument("--px4_sys_id", type=str, required=True, help="PX4系统ID")

    # 解析命令行参数
    args = parser.parse_args()

    # 生成并打印主机名
    hostname = generate_hostname(args.prefix, args.drone_type, args.px4_sys_id)
    print(f"生成的主机名: {hostname}")
    # set hostname 
    # 设置系统主机名 set_hostname(hostname)