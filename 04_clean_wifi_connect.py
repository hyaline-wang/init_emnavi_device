import subprocess
import os,sys
def is_root():
    return os.geteuid() == 0
def delete_all_wifi_connections():
    try:
        # Get the list of all Wi-Fi connections
        result = subprocess.run(['nmcli', '-t', '-f', 'NAME,TYPE', 'connection', 'show'], capture_output=True, text=True)
        connections = result.stdout.strip().split('\n')

        # Delete each Wi-Fi connection
        for connection in connections:
            name, conn_type = connection.split(':')
            if conn_type == '802-11-wireless':  # Ensure the connection type is Wi-Fi
                subprocess.run(['nmcli', 'connection', 'delete', name])
                print(f"Deleted Wi-Fi connection: {name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if not is_root():
        print("该脚本需要以 root 权限执行。请使用 sudo 运行。")
        sys.exit(1)
    delete_all_wifi_connections()