#!/usr/bin/python3

import json
#import serial
import threading
import time
from config import *

class serial_op(threading.Thread):
    def __init__(self, threadID, name, cfg):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cfg = cfg

    def run(self):
        print(self.cfg)

if __name__ == "__main__":
    test = serial_op(1, "test", config.config['COM1'])
    test.start()
    test.join()

    time.sleep(2)

