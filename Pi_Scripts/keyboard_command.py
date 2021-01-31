import RPi.GPIO as GPIO
from gpiozero import Button, LED
from pynput.keyboard import Key, Controller
from signal import pause
import time


def action1(self):
    keyboard.press(Key.right)
    keyboard.release(Key.right)


def action2(self):
    keyboard.press(Key.left)
    keyboard.release(Key.left)


def action3(self):
    keyboard.type("Greetings Mortals ")


def action4(self):
    led.toggle()


if __name__ == '__main__':
    button1_pin = 17
    button2_pin = 27
    button3_pin = 22
    led = LED(10)
    keyboard = Controller()

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(button3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(button1_pin, GPIO.BOTH, callback=action1, bouncetime=800)
    GPIO.add_event_detect(button2_pin, GPIO.BOTH, callback=action2, bouncetime=800)
    GPIO.add_event_detect(button3_pin, GPIO.BOTH, callback=action4, bouncetime=800)

    while True:
        print("Waiting for button")

