import serial
import time

port= serial.Serial('/dev/ttyAMA0',4800,timeout=100)
port.close()
if(port.isOpen()==False):
	print("in")
	port.open()
port.flushOutput()
port.flushInput()
time.sleep(1)
while True:
	stri=port.read(5)
	port.write(stri)
	time.sleep(1)
	print(stri)
port.close()