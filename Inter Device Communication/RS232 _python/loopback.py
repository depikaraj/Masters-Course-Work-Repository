#!/usr/bin/python3

from serial import Serial
import time
import sys; print(sys.version)

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
outStr=input("Enter data to be transmitted: ")
outStr=outStr.encode()
serialPort.setRTS(1)
serialPort.write(outStr)
    #time.sleep(0.05)
ct=serialPort.getCTS()
if serialPort.getCTS():
	inStr = serialPort.read(len(outStr)) 
#print(ct)
inStr=inStr.decode()

#print("Serial Port Input is :",inStr)
outStr=outStr.decode()
print("Outpust string = " + outStr)
if(inStr == outStr):
        print ("Loop back Test WORKED! for length of ",len(outStr))
else:
        print("failed")

serialPort.close()
