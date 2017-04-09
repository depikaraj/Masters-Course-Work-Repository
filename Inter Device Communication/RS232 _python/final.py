#!/usr/bin/env python3
#transmitting
# Final without rx and tx 
from serial import Serial
import bitarray
import time
import sys; print(sys.version)
import bitarray
print('\nDemonstrating M2M communication using RS232\n')

serialPort = Serial("/dev/ttyUSB2")#timeout after 5 seconds

if (serialPort.isOpen() == False):
    serialPort.open()

ba = bitarray.bitarray()
ba.fromstring('1234567890PDB-->RS232')

serialPort.setDTR(0)

for ch in ba:	
	serialPort.setRTS(ch)
	time.sleep(0.1)
	
	

serialPort.setDTR(1)
time.sleep(0.5)	


serialPort.close()
