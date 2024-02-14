import os, json
import time

# python 3.x
from configparser import ConfigParser

config = ConfigParser()


def test1():
    print("OK")


ok = True

while ok:
    config.read("test.cfg")
    arr_reboot = config.get("HOUR", "REBOOT_HOURS")
    # list(config.get("HOURS", "RESET_HOURS"))
    arr_reset = tuple(json.loads(config.get("HOUR", "RESET_HOURS")))
    print("ARR:", arr_reset[2])
    time.sleep(1)


k = input("Press q to exit")
