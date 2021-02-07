import platform  
import subprocess 

# Raspberry Pi Information
ip_address = "192.168.1.102"
username = "pi"
password = "raspberry"


def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    Always return True on Windows Machine.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

if __name__ == '__main__':
    print(ping(ip_address))
    subprocess.call('`feh -F -d --slideshow-delay 10 --action1 "python3 /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/feh_image_deletion.py -d echo @$PWD/@%n %n"`'.replace("@", "'"))
