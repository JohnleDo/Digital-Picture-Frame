import RPi.GPIO as GPIO
from gpiozero import Button, LED
from signal import pause
import time
from datetime import datetime
import os
from pynput.keyboard import Key, Controller


def WriteToLog(logFilePath, message):
    if (os.path.exists(logFilePath)):
        with open(logFilePath, "a") as file:
            file.write(datetime.today().strftime("%d-%b-%Y (%H:%M:%S)") + ": " + message + "\n")
            file.close()
    
    else:
        with open(logFilePath, "w") as file:
            file.write(datetime.today().strftime("%d-%b-%Y (%H:%M:%S)") + ": " + message + "\n")
            file.close()

# Control the right key to move forward in FEH slideshow
def action1(self):
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    WriteToLog(logFilePath, "Moved Forward")

# Control the left key to move backward in FEH slideshow
def action2(self):
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    WriteToLog(logFilePath, "Moved Backward in FEH Slideshow")

# Control the h key to pause/resume the FEH slideshow
def action3(self):
    keyboard.press('h')
    keyboard.release('h')
    WriteToLog(logFilePath, "Paused FEH")

# Control the action-binded key "1" to delete the current image
def action4(self):
    keyboard.press('1')
    keyboard.release('1')
    WriteToLog(logFilePath, "Deleted Image")

# Control the escape key to exit slideshow.
def action5(self):
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    WriteToLog(logFilePath, "Exitted Program")

# Shuts Down Raspberry Pi
def action6(self):
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    WriteToLog(logFilePath, "Exitted Program and Shutdown")
    os.system("shutdown now -h")


if __name__ == '__main__':
    logFilePath = os.getcwd() + "/Logs/Keyboard_Command_Log.txt"
    WriteToLog(logFilePath, "Program Started")
    keyboard = Controller()
    button1_pin = 2
    button2_pin = 3
    button3_pin = 4
    button4_pin = 17
    button5_pin = 27
    button6_pin = 22

    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button5_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(button6_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=action1, bouncetime=500)
        GPIO.add_event_detect(button2_pin, GPIO.BOTH, callback=action2, bouncetime=500)
        GPIO.add_event_detect(button3_pin, GPIO.BOTH, callback=action3, bouncetime=500)
        GPIO.add_event_detect(button4_pin, GPIO.BOTH, callback=action4, bouncetime=500)
        GPIO.add_event_detect(button5_pin, GPIO.BOTH, callback=action5, bouncetime=500)
        GPIO.add_event_detect(button6_pin, GPIO.BOTH, callback=action6, bouncetime=500)

        while True:
            time.sleep(1)
    except Exception as e:
        WriteToLog(logFilePath,"[ERROR]: " + e.args[0])

