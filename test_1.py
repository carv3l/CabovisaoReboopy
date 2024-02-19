import os, json
import time

import datetime

# python 3.x
from configparser import ConfigParser

config = ConfigParser()


def test1():
    print("OK")


ok = True

while ok:

    HOUR = datetime.datetime.now().hour   # the current hour
    MINUTE = datetime.datetime.now().minute # the current minute
    SECONDS = datetime.datetime.now().second #the current second
    MILISECONDS = datetime.datetime.now().microsecond #the current second
    WEEKDAY = datetime.datetime.now().weekday()

    print("DAY",WEEKDAY )

    config.read("test.cfg")
    
    arr_reset = tuple(json.loads(config.get("HOUR", "RESET_HOURS")))

    # arr_reboot = tuple(json.loads(config.get("HOUR", "REBOOT_HOURS")))
    arr_weekdays = tuple(json.loads(config.get("WEEK", "WEEK_DAYS")))

    if (WEEKDAY in arr_weekdays):
        print("HOUR", HOUR)
        if (str(HOUR) in arr_reset):
            print("MATCH, resetting....")
    time.sleep(1)


k = input("Press q to exit")
