import os
import sys
import time
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--restart", help="restart the browser if it exits. Use Cntr + C to exit.",
    action="store_true")
parser.add_argument("-v", "--verbose", help="Enable verbose output",
    action="store_true")
args = parser.parse_args()

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
            print("[parent] waiting")
            time.sleep(1.5)
    else:
        # child
        print("[child] running " + command)
        ret = os.system(command);
        #ret = os.execlp("chromium-browser", command) # Dit werkt niet?
        print(ret)
        exit(ret)

if __name__ == "__main__":
    main()
else:
    print(__name__)
