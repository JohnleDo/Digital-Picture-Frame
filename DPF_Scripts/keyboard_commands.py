import argparse
from pynput.keyboard import Key, Controller

# Control the right key to move forward in FEH slideshow
def action1():
    keyboard.press(Key.right)
    keyboard.release(Key.right)

# Control the left key to move backward in FEH slideshow
def action2():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

# Control the h key to pause/resume the FEH slideshow
def action3():
    keyboard.press('h')
    keyboard.release('h')

# Control the action-binded key "1" to delete the current image
def action4():
    keyboard.press('1')
    keyboard.release('1')

# Control the escape key to exit slideshow.
def action5():
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)

if __name__ == '__main__':
    keyboard = Controller()

    parser = argparse.ArgumentParser(description='used to send keystrokes to DPF machine')
    parser.add_argument('-a', '--action',help='An integer value that corresponds to an action')
    args = parser.parse_args()

    if args.action == "1":
        action1()
    elif args.action == "2":
        action2()
    elif args.action == "3":
        action3()
    elif args.action == "4":
        action4()
    elif args.action == "5":
        action5()
    else:
        print("Invalid Action")
