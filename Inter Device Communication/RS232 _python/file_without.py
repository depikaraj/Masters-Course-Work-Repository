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
wfile=open("Out.txt","w")

while (serialPort.getDSR()):
#print("Receiving...")
	pass
#serialPort.getCTS()
#start=time.time()
for i in range(0,40) :

	st.append(serialPort.getCTS())
	time.sleep(1)

#print(st)
#end=time.time()
#print("Time Taken is ",(end-start))
print("Received Output without Rx and Tx is:")

try:
	print(st)	
	print(st.tostring())
	wfile.write(st.decode())

except:
	print(st)


	
l = len(st)
#print("Recieved a file of size", l, "in time", end-start)
#print("No of 1s=", st.count())
#print("No of 0s=", len(st)-st.count())
one = st.count()/84
zero = (len(st)-st.count())/92
#print("Accuracy is", (one+zero)/2 * 100 )
serialPort.close()

