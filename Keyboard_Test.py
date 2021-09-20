import RPi.GPIO as GPIO
from gpiozero import Button, LED
import time

def action1(self):
    print("Button 1 was pressed")

def action2(self):
    print("Button 2 was pressed")

def action3(self):
    print("Button 3 was pressed")

def action4(self):
    print("Button 4 was pressed")

def action5(self):
    print("Button 5 was pressed")

def action6(self):
    print("Button 6 was pressed")


if __name__ == '__main__':
    print("Please Press a button")
    button1_pin = 2
    button2_pin = 3
    button3_pin = 4
    button4_pin = 17
    button5_pin = 27
    button6_pin = 22

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
    