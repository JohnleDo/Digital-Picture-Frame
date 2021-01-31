from gpiozero import LightSensor
import RPi.GPIO as GPIO
import time

ldr = LightSensor(4)
GPIO.setmode(GPIO.BCM)
GPIO.setup(10, GPIO.OUT)

led = GPIO.PWM(10, 500)
led.start(0)

while(True):
    print(ldr.value * 100)
    led.ChangeDutyCycle(ldr.value * 100)
    time.sleep(0.1)
"""
while(1):
    for dc in range(0, 101, 5):
        led.ChangeDutyCycle(dc)
        time.sleep(0.1)
        
    for dc in range(100, -1, -5):
        led.ChangeDutyCycle(dc)
        time.sleep(0.1)
"""


