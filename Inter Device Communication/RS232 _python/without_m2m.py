#!/usr/bin/python3
#Receieving side
#Final without RX and TX basic
from serial import Serial
import bitarray
import time
import binascii

serialPort = Serial("/dev/ttyUSB2",baudrate= 9600,timeout=10)

if (serialPort.isOpen() == False):
    serialPort.open()

st=bitarray.bitarray()

while (serialPort.getDSR()):
#print("Receiving...")
	pass

#start=time.time()
for i in range(0,8):

	st.append(serialPort.getCTS())
	time.sleep(1)

#print(st)
#end=time.time()
#print("Time Taken is ",(end-start))
print("Received Output without Rx and Tx is:")


print(st.tostring())

print(st)


serialPort.close()

