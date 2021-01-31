import argparse
from pynput.keyboard import Key, Controller

def action1():
    keyboard.press(Key.right)
    keyboard.release(Key.right)


def action2():
    keyboard.press(Key.left)
    keyboard.release(Key.left)

def action3():
    keyboard.type("Greetings Mortals ")

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
    else:
        print("Invalid Action")