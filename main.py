import os
import sys
import time
import argparse
from pynput.keyboard import Key, Controller
keyboard = Controller()

parser = argparse.ArgumentParser()
parser.add_argument("--restart", help="restart the browser if it exits. Use Cntr + C to exit.",
    action="store_true")
parser.add_argument("-v", "--verbose", help="Enable verbose output",
    action="store_true")
parser.add_argument("-d", "--delay", help="Set delay between switching tabs. Default is 10s.",)
args = parser.parse_args()

delay = 5
if args.delay:
    print(args.delay)
    delay = args.delay;
    print(delay)

def main():

    # Maak lijst met urls om te laden
    file = open("sites", "r")
    urls:str = ""
    for line in file:
        if args.verbose:
            print(line)
        urls += line.rstrip("\n")
        urls += " "
    if args.verbose:
        print(urls) # test


    # Maak command om browser te starten
    #command = urls + " --kiosk"
    command = "chromium-browser " + urls + " --kiosk "

    if args.verbose:
        print(command)

    pid = os.fork() # pid is pid van child
    if pid:
        # parent
        while True:
            try:
                print("[parent] waiting")
                time.sleep(delay)
                with keyboard.pressed(Key.ctrl_l):
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
            except KeyboardInterrupt:
                os.system("kill " + str(pid))
                exit(1)

    else:
        # child
        print("[child] running " + command)
        ret = os.system(command);
        print("Browser exited with code: " + str(ret))
        exit(ret)

if __name__ == "__main__":
    main()
else:
    print(__name__)
