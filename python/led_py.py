#!/usr/bin/env python
# -*- coding:utf-8 -*-

import mraa
import time

print("Hello mraa\nVersion: %s" % mraa.getVersion())

gpio = mraa.Gpio(20)
gpio.dir(mraa.DIR_OUT)

for i in range(5):
    gpio.write(1)
    time.sleep(1)

    gpio.write(0)
    time.sleep(1)

gpio.dir(mraa.DIR_IN)