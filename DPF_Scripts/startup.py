"""
This is the script for getting everything up and running. These are the steps it goes through:
1. Check if Raspberry Pi is fully turned on and connected. If not, it will continue to ping it till its pingable.
2. Execute the Raspberry Pi script to allow for our buttons to work.
3. Finally, it will start the Slideshow.
"""

import platform  
import subprocess
import os 

# Raspberry Pi Information
ip_address = "192.168.1.102"
username = "pi"
password = "raspberry"

# The path to the directory holding all the images for the slideshow
image_directory = "/home/dpf/Desktop/Slideshow Images"


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
    while ping(ip_address) is False:
        print("Could not reach Raspberry Pi, ")
    os.chdir(image_directory)
    subprocess.call('`feh -F -d --slideshow-delay 10 --action1 "python3 /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/feh_image_deletion.py -d echo @$PWD/@%n %n"`'.replace("@", "'"))
