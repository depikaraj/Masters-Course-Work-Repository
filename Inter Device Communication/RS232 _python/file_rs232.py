#!/usr/bin/python3

from serial import Serial
import time

rfile=open("txdata","r")
wfile=open("rxdata","w")
serialPort = Serial("/dev/ttyUSB0", timeout=10)
serialPort.baudrate=input("Enter Baud rate: ")
serialPort.rtscts=True
if (serialPort.isOpen() == False):
    serialPort.open()

outStr = ''
inStr = ''

serialPort.flushInput()
serialPort.flushOutput()

#for i, a in enumerate(range(33, 126)):
# outStr += chr(a)
outStr=rfile.read()
outStr=outStr.encode()
time.sleep(1)
serialPort.setRTS(1)
serialPort.write(outStr)
    #time.sleep(0.05)
ct=serialPort.getCTS()
if serialPort.getCTS():
	inStr = serialPort.read(10000) 

inStr=inStr.decode()

wfile.write(inStr)
print("Serial Port Input is : ",inStr)
outStr=outStr.decode()


serialPort.close()
rfile.close()
wfile.close()
