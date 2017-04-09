#!/usr/bin/env python3
#Driver for checcking baud rate 
from serial import Serial
import bitarray
import time
import sys; print(sys.version)

serialPort = Serial("/dev/ttyUSB1", timeout=5)#timeout after 5 seconds
print('Automatic Baudrate detector : Senders side ')
serialPort.baudrate=input("Enter Baud rate: ")#baud rate
serialPort.stopbits=1;#1 stop bit
#serialPort.rtscts=True
serialPort.setRTS(1)
if (serialPort.isOpen() == False):
    serialPort.open()       
outStr = ''
inStr = ''
serialPort.flushInput()
serialPort.flushOutput()

print('Sending A to the other side continuosly. Compute the baud rate')
while True:
	outStr='U'
	outStr=outStr.encode()#encode the strin
	serialPort.write(outStr)
	time.sleep(1)

serialPort.close()


