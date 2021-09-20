import RPi.GPIO as GPIO
from gpiozero import Button, LED
from signal import pause
import time
import paramiko

#  Control the right key to move forward in FEH slideshow
def action1(self):
    create_ssh(host, username, password, "1")


# Control the left key to move backward in FEH slideshow
def action2(self):
    create_ssh(host, username, password, "2")


# Control the h key to pause/resume the FEH slideshow
def action3(self):
    create_ssh(host, username, password, "3")


# Control the action-binded key "1" ti delete the current image
def action4(self):
    create_ssh(host, username, password, "4")


# Control the escape key to exit the slideshow
def action5(self):
    create_ssh(host, username, password, "5")


# This function is for sshing into a machine and then executing a command on it
def create_ssh(host, username, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    try:
        ssh.connect(host, username=username, password=password)
    finally:
        stdin, stdout, stderr = ssh.exec_command("DISPLAY=':0' python3 /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/keyboard_commands.py -a {}".format(command))
        print("Action " + command + " executed.")
        ssh.close()


if __name__ == '__main__':
    button1_pin = 2
    button2_pin = 3
    button3_pin = 4
    button4_pin = 17
    button5_pin = 27

    
    host = "192.168.1.100"
    username = "dpf"
    password = "111696"

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=action1, bouncetime=1500)
    GPIO.add_event_detect(button2_pin, GPIO.BOTH, callback=action2, bouncetime=1500)
    GPIO.add_event_detect(button3_pin, GPIO.BOTH, callback=action3, bouncetime=1500)
    GPIO.add_event_detect(button4_pin, GPIO.BOTH, callback=action4, bouncetime=1500)
    GPIO.add_event_detect(button5_pin, GPIO.BOTH, callback=action5, bouncetime=1500)

    while True:
        time.sleep(1)

