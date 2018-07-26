#!/usr/bin/python3

import threading
import re
import time

class sd_detect(threading.Thread):
    def __init__(self, name, event):
        threading.Thread.__init__(self)
        self.name = name
        self.event = event

    def run(self):
        while True:
            with open("/proc/mounts", "r") as f:
                str = f.read()

            reval = re.search("/dev/mmcblk0p1", str)
            if bool(reval):
                self.event.set()
                try :
                    with open("/sys/class/gpio/gpio29/value", "w") as led_value:
                        led_value.write("1")
                except :
                    pass
            else:
                self.event.clear()
                try :
                    with open("/sys/class/gpio/gpio29/value", "w") as led_value:
                        led_value.write("0")
                except :
                    pass

            time.sleep(0.5)

if __name__ == "__main__" :
    event = threading.Event()
    test = sd_detect("chen_test", event)
    test.start()
    test.join()

