import os
import subprocess

def clean_cache_root():
    # Clear bash history for root and emnavi
    with open('/root/.bash_history', 'w'):
        pass
    subprocess.run('bash -c "history -c"', shell=True, check=True)
    # Remove temporary files
    subprocess.run(['rm', '-rf', '/tmp/*'], check=True)
    subprocess.run(['rm', '-rf', '/root/.cache/*'], check=True)
    # Remove log files
    subprocess.run(['sudo', 'rm', '-rf', '/var/log/*'], check=True)
    # Vacuum journal logs
    subprocess.run(['journalctl', '--vacuum-time=1d'], check=True)
    # Clean apt cache
    subprocess.run(['apt', 'clean'], check=True)
def clean_cache_user(username):

    with open('/home/emnavi/.bash_history', 'w'):
        pass
    # Remove cache directories
    subprocess.run(['rm', '-rf', '/home/emnavi/.cache/*'], check=True)
    

if __name__ == "__main__":
    clean_cache_root()
    clean_cache_user('emnavi')