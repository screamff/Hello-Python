#!/usr/bin/env python
#coding:utf-8
import serial
ser = serial.Serial('COM6', 38400, stopbits=serial.STOPBITS_TWO,  timeout=None)
print ser.portstr
x = [0x80,0x03,0x00,0x00,0x00,0x08,0x5a,0x1d]
y = map(chr, x)
while 1:
    try:
        ser.write(y)
        raw_data =  map(str, ser.read(21))
        # print raw_data
        a = ord(raw_data[-4])
        b = ord(raw_data[-3])
        print a*2**8+b
    except KeyboardInterrupt:
        ser.close()
        break
