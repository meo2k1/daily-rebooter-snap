import os

import schedule
import time
import re
import sys

def reboot(t):
    os.system('dbus-send --system --print-reply --dest=org.freedesktop.login1 /org/freedesktop/login1 "org.freedesktop.login1.Manager.Reboot" boolean:true')
    os.system("sudo reboot")

str = "00:00"

snap_data = "." if 'SNAP_DATA' not in os.environ else os.environ['SNAP_DATA']
fname = snap_data + "/config.txt"
if os.path.isfile(fname):
    with open(fname, "r") as f:
        line = f.readline();
        if (line.startswith("off")):
            print(f"Switch off!")
            sys.exit(0);
        tmp = re.sub(r'[^0-9:]', '', line);
        try:
            d = time.strptime(tmp, '%H:%M')
            str = f'{d.tm_hour:02}:{d.tm_min:02}'
            print(f"Valid time read: {str}")
        except (ValueError, OSError):
            print(f"This is not a valid time: {tmp}...\nUse Format HH:MM or \"off\"...")

else:
    print("Couldn't find a config file... Defaulting to 00:00...")

   
schedule.every().day.at(str).do(reboot,'Rebooting now...')

while True:
    schedule.run_pending()
    time.sleep(20) # wait 10 seconds
