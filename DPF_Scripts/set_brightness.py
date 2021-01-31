import pexpect
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='used to increase/decrease screen brightness via backlight')
    parser.add_argument('-b', '--brightness',help='An integer value to set the brightness of monitor.')
    args = parser.parse_args()

    command = pexpect.spawn("sudo ddcutil setvcp 10 {}".format(args.brightness))
    command.expect("password")
    command.sendline("111696")
