#!/usr/bin/python3

import configparser
import os
import json
import time

class configure():

    __configure_file_path = "Serial_op/config.json";

    def __new__(cls, *args, **kwargs):

        if not hasattr(cls, "_inst"):

            cls._inst = super(configure, cls).__new__(cls);

            try :
                json_data = open(cls.__configure_file_path);
            except :
                cls.__configure_file_path = "../Serial_op/config.json"
                json_data = open(cls.__configure_file_path);
                print("use other file path");

            cls.config = json.load(json_data);

        return cls._inst;

    def print_cfg(cls):
        print(cls.config);

    def set_file_path(cls, filepath):
        cls.__configure_file_path = filepath;

config = configure();

if __name__ == '__main__':
    config.set_file_path("Serial_op/config.json");
    config.print_cfg();
