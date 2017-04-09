#!/usr/bin/python3
#Receieving side
#Final without RX and TX basic
from serial import Serial
import bitarray
import time

serialPort = Serial("/dev/ttyUSB1",baudrate= 9600,timeout=10)

if (serialPort.isOpen() == False):
    serialPort.open()

st=bitarray.bitarray()

while (serialPort.getDSR()):
	print("Receiving...")
	pass

start=time.time()
while(1):
	if(serialPort.getDSR()):
		break;
	st.append(serialPort.getCTS())
	time.sleep(0.1)
	#	print("here")

#print(st)
end=time.time()
print(st)
print("Time Taken is ",(end-start))
print("Received Output without Rx and Tx is:")

try:
	print(st.tostring())

except:
	print(st)

print("No of 1s=", st.count())
print("No of 0s=", len(st)-st.count())
one = st.count()/84
zero = (len(st)-st.count())/92
print("Accuracy is", (one+zero)/2 * 100 )
serialPort.close()

