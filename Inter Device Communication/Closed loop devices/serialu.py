import serial
import time

ser= serial.Serial('/dev/ttyACM0',4800,timeout=100)
port= serial.Serial('/dev/ttyAMA0',4800,timeout=100)
ser.close()
if(ser.isOpen()==False):
	ser.open()
port.close()
if(port.isOpen()==False):
	port.open()
ser.flushInput()
port.flushOutput()
time.sleep(1)
while True:
	stri=ser.read(1)
	port.write("Completed")
	time.sleep(1)
	print(stri)
ser.close()
port.close()