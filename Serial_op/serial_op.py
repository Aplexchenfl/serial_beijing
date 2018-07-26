#!/usr/bin/python3

import json
import serial
import threading
import time
import os
from Serial_op.config import *

serial_op_lock = threading.Lock()

class serial_op(threading.Thread):
    def __init__(self, name, cfg, event):
        threading.Thread.__init__(self)
        self.event = event
        self.name = name
        self.cfg = cfg
        self.ser = serial.Serial(self.cfg['port'], self.cfg['baudrate'], timeout = self.cfg['timeout'])

    def readmsg_to_sd(self):
        while True:
            if self.event.is_set():
                self.recvmsg = self.ser.read(size = 64)

                if (len(self.recvmsg) > 0):
                    serial_op_lock.acquire()
                    #print(self.recvmsg)
                    try :
                        with open(self.file_name, "ab+") as f :
                            f.write(self.recvmsg)
                    except :
                        print("write error")
                        pass
                    serial_op_lock.release()

                #print("run thread ~~")
            else:
                self.get_file_name()
                pass

    def get_file_name(self):
        #self.file_name = "/root/sd_data/" + str(round(time.time())) + ".txt"
        file_name = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.file_name = "/root/sd_data/" + file_name + ".txt"

        #print(self.file_name)

    def run(self):
        self.get_file_name()
        self.readmsg_to_sd()
        print(self.cfg)

if __name__ == "__main__":
    test = serial_op("test", config.config['COM1'])
    test.start()
    test.join()

    time.sleep(2)

