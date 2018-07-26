#!/usr/bin/python3

from Serial_op.serial_op import *

if __name__ == "__main__":
    test1 = serial_op(1, "test1", config.config['COM1'])
    test2 = serial_op(2, "test2", config.config['COM2'])

    test1.start()
    test2.start()

    test1.join()
    test2.join()

    time.sleep(2)

