from datetime import datetime, time
import pytz


if __name__ == '__main__':    
    current_time = datetime.now(pytz.timezone('America/Chicago'))
    """  
    print ("The current time is: ")  
    print (current_time.strftime("%I:%M %p"))
    print(current_time.time())
    d = datetime.strptime("1:30", "%H:%M")
    print(d.strftime("%I:%M %p"))
    print(d.time())
    """


    # Set to turn off display between 9:00pm to 9:00am
    if current_time.time() >= time(21,00) or current_time.time() <= time(9,00):
        print("==============================")
        print("Screen is currently off")
        print("Current Time: " + current_time.strftime("%I:%M %p"))
        print("==============================")
    else:
        print("==============================")
        print("Screen is currently on")
        print("Current Time: " + current_time.strftime("%I:%M %p"))
        print("==============================")