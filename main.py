#!/usr/bin/python3

from Serial_op.serial_op import *
import threading
from Sd_mount_detect.sd_mount_detect import *

if __name__ == "__main__":
    event = threading.Event()
    test1 = serial_op("test1", config.config['COM1'], event)
    test2 = serial_op("test2", config.config['COM2'], event)

    test3 = sd_detect("chen_test", event)
    test3.start()
    test1.start()
    test2.start()

    test1.join()

    time.sleep(2)

