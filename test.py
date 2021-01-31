import pexpect
child = pexpect.spawn("sudo ddcutil setvcp 10 0")
child.expect("password")
child.sendline("111696")
print(child.read())
