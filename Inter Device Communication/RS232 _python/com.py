#!/usr/bin/env python3
#M2M with rx and tx chat 
from serial import Serial
import bitarray
import time
import sys; print(sys.version)

serialPort = Serial("/dev/ttyUSB1", timeout=5)#timeout after 5 seconds
serialPort.baudrate=input("Enter Baud rate: ")#baud rate
serialPort.stopbits=1;#1 stop bit
serialPort.rtscts=True
if (serialPort.isOpen() == False):
    serialPort.open()

outStr = ''
inStr = ''

serialPort.flushInput()
serialPort.flushOutput()
print( 'Demonstrating M2M using RS232. Press -1 to exit \n')
while True:
	outStr=input("Enter data to be transmitted: ")
	if(outStr=='-1'):
		print('Exiting \n')
		break		
	outStr=outStr.encode()#encode the string	
	serialPort.setRTS(1)
	serialPort.write(outStr)
	ct=serialPort.getCTS()
	if serialPort.getCTS():
	    inStr = serialPort.read(10) 
	inStr=inStr.decode()
	print("Serial port input : " + inStr)
serialPort.close()


