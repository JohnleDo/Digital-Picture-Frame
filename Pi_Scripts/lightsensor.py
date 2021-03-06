import paramiko
from contextlib import contextmanager
import RPi.GPIO as GPIO
import time
import re

current_brightness = 0

def rc_time (ldr):
    count = 0
  
    # Output on the pin for 
    GPIO.setup(ldr, GPIO.OUT)
    GPIO.output(ldr, GPIO.LOW)
    time.sleep(0.1)

    # Change the pin back to input
    GPIO.setup(ldr, GPIO.IN)
  
    # Count until the pin goes high
    while (GPIO.input(ldr) == GPIO.LOW):
        count += 1

    return count


# Converts the LDR value we got into a 0-100 range. The lower the value the less light the LDR detects while
# the higher the value the amount of light detected.
# 0 = Dark, 100 = Light 
def convert_value(value, top_range, low_range):
    if value >= top_range:
        return (100 - 100) * -1
    elif value <= low_range:
        return (0 - 100) * -1
    else:
        return (((value / top_range) * 100) - 100) * -1

# Controls the LED with a fading effect instead of an instant change
def control_brightness(converted_old_value, converted_new_value):
    if converted_old_value < converted_new_value:
        for x in range(round(converted_old_value), round(converted_new_value), 15):
            print(x)
            create_ssh(host, username, password, x)
        create_ssh(host, username, password, round(converted_new_value))
        current_brightness = round(converted_new_value)
        print(round(converted_new_value))

    elif converted_old_value > converted_new_value:
        for x in range(round(converted_old_value), round(converted_new_value), -15):
            print(x)
            create_ssh(host, username, password, x)
        create_ssh(host, username, password, round(converted_new_value))
        current_brightness = round(converted_new_value)
        print(round(converted_new_value))
    else:
        print("No Change")


def create_ssh(host, username, password, value):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    output = ""
    try:
        #print("creating connection")
        ssh.connect(host, username=username, password=password)
        #print("connected")
    finally:
        stdin, stdout, stderr = ssh.exec_command("python3 /home/dpf/Desktop/Digital-Picture-Frame/DPF_Scripts/set_brightness.py -b {}".format(value))
        for line in stdout:
            output += line

        result = re.search("current value = +[0-9]+", output).group(0)
        result = result.replace("current value =", "").strip()
        print("Current brightness value: " + result)
        #print("closing connection")
        ssh.close()
        #print("closed")
       
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)

    #define the pin that goes to the circuit
    ldr = 7
    
    host = "192.168.1.100"
    username = "dpf"
    password = "111696"

    # This while loop is for checking the raw value of the ldr. Good to use to adjust the top_value
    # and low value in the convert_value function.
    while True:
      print(rc_time(ldr))

    # Catch when script is interupted, cleanup correctly
    # We use Pin 19 (GPIO 10) for LED due to setting the board to analog earlier
    try:
        old_value = rc_time(ldr)
        set_value = round(convert_value(old_value, 5000, 300))
        print("Setting brightness value: " + str(set_value))
        create_ssh(host, username, password, set_value)
        current_brightness = int(set_value)
        
        # Main loop
        while True:
            new_value = rc_time(ldr)
            
            converted_old_value = convert_value(old_value, 5000, 300)
            converted_new_value = convert_value(new_value, 5000, 300)
            print("Old Value: " + str(converted_old_value))
            print("New Value: "+ str(converted_new_value))
            if ((converted_old_value - converted_new_value) >= 20) or ((converted_new_value - converted_old_value) >= 20) or (converted_new_value == 0 and current_brightness != 0) or (converted_new_value == 100 and current_brightness != 100):
                #print("One of the conditions met, changing now")
                control_brightness(converted_old_value, converted_new_value)
            time.sleep(5)
            old_value = new_value
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
    
