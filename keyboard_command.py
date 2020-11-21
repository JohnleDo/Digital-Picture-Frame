import RPi.GPIO as GPIO
from gpiozero import Button
from pynput.keyboard import Key, Controller
from signal import pause
import time


def action1(self):
    keyboard.type("Tina is not cool ")

def action2(self):
    keyboard.type("Tina is soooooo cool ")

tiny_button_pin = 17
big_button_pin = 27
keyboard= Controller()

GPIO.setmode(GPIO.BCM)
GPIO.setup(tiny_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(big_button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(tiny_button_pin, GPIO.BOTH, callback=action1,bouncetime=800)
GPIO.add_event_detect(big_button_pin, GPIO.BOTH, callback=action2, bouncetime=800)

while True:
    print("Waiting for button")

