#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time


"""
This Sets the Board to the actual Analog Pin Number and not the Digital Pin Number
Example, GPIO 4 where the 4 is the digital number while the analog number is 7 if you reference
GPIO Header Quick Reference sheet.

Also another reason for this is because we want to use the Analog Pin to see how quickly our
capactior charges up to get a better read on the LDR.
"""
GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
ldr = 7


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


# Converts the LDR value we got into a 0-100 range.
def convert_value(value, top_range, low_range):
    if value >= top_range:
        return 100
    elif value <= low_range:
        return 0
    else:
        return (value / top_range) * 100

# Controls the LED with a fading effect instead of an instant change
def control_led(converted_old_value, converted_new_value):
    if converted_old_value < converted_new_value:
        for x in range(round(converted_old_value), round(converted_new_value)):
            print(x)
            led.ChangeDutyCycle(x)
            time.sleep(.0075)
    elif converted_old_value > converted_new_value:
        for x in range(round(converted_old_value), round(converted_new_value), -1):
            print(x)
            led.ChangeDutyCycle(x)
            time.sleep(.0075)
    else:
        led.ChangeDutyCycle(converted_new_value)
        

# Catch when script is interupted, cleanup correctly
# We use Pin 19 (GPIO 10) for LED due to setting the board to analog earlier
try:
    GPIO.setup(19, GPIO.OUT)
    led = GPIO.PWM(19, 500)
    led.start(0)
    old_value = rc_time(ldr)
    # Main loop
    while True:
        new_value = rc_time(ldr)
        
        converted_old_value = convert_value(old_value, 50000, 1000)
        converted_new_value = convert_value(new_value, 50000, 1000)
        print("Old Value: " + str(converted_old_value))
        print("New Value: "+ str(converted_new_value))
        if ((converted_old_value - converted_new_value) >= 20) or ((converted_new_value - converted_old_value) >= 20) or converted_new_value == 0 or converted_new_value == 100:
            print("One of the conditions met, changing now")
            control_led(converted_old_value, converted_new_value)
        time.sleep(1)
        old_value = new_value
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
