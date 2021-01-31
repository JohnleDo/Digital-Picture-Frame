import paramiko
from contextlib import contextmanager


def create_ssh(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    try:
        print("creating connection")
        ssh.connect(host, username=username, password=password)
        print("connected")
    finally:
        stdin, stdout, stderr = ssh.exec_command("sudo ddcutil setvcp 10 0")
        for line in stdout:
            print(line)
        
        print("closing connection")
        ssh.close()
        print("closed")

def test():
    print("1")
       
if __name__ == '__main__':
    host = "192.168.1.100"
    username = "dpf"
    password = "111696"
    create_ssh(host, username, password)
    