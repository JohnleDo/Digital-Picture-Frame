"""
This is the script for getting everything up and running. These are the steps it goes through:
1. Check if Raspberry Pi is fully turned on and connected. If not, it will continue to ping it till its pingable.
2. Execute the Raspberry Pi script to allow for our buttons to work.
3. Finally, it will start the Slideshow.
4. As the Slideshow runs it will keep track of the current time to make sure that when the machine goes to sleep that
   everything is paused and monitor goes to sleep.
"""

import platform  
import subprocess
import os
import pexpect
import datetime
import pytz

# Raspberry Pi Information
ip_address = "192.168.1.102"
username = "pi"
password = "raspberry"

# The path to the directory holding all the images for the slideshow
image_directory = "/home/dpf/Desktop/Slideshow Images"


def control_monitor(control):
    if control == "Turn On":
        command = pexpect.spawn("sudo ddcutil setvcp D6 01")
        command.expect("password")
        command.sendline("111696")
        command.read()
    elif control == "Turn Off":
        command = pexpect.spawn("sudo ddcutil setvcp D6 04")
        command.expect("password")
        command.sendline("111696")
        command.read()

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    Note: Always return True on Windows Machine.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

if __name__ == '__main__':
    """
    while ping(ip_address) is False:
        print("Could not reach Raspberry Pi, ")
    os.chdir(image_directory)
    os.system("bash /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/slideshow_command.sh")
    """
    current_time = datetime.datetime.now(pytz.timezone('America/Chicago'))  
    print ("The current time is: ")  
    print (current_time.strftime("%I:%M %p"))
