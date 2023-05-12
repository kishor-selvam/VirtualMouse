from subprocess import call
def prLightPurple(skk): print("\033[94m {}\033[00m".format(skk))
def prGreen(skk): print("\033[92m {}\033[00m".format(skk))
def prYellow(skk): print("\033[93m {}\033[00m".format(skk))
def prRed(skk): print("\033[91m {}\033[00m".format(skk))

def open_mouse():
    call(["python","Mouse.py"])
def open_keyboard():
    call(["python","Keyboard.py"])

while 1:
    print("")
    prLightPurple("          VIRTUAL MOUSE AND VIRTUAL KEYBOARD")
    prGreen("1.VIRTUAL MOUSE\n 2.VIRTUAL KEYBOARD")
    print("")
    user_ip = input(str(" ENTER OPTION :"))
    print("")
    if user_ip == "1":
        open_mouse()
    elif user_ip == "2":
        open_keyboard()
    else:
        prRed("Please Enter Valid Option")
    print("")
