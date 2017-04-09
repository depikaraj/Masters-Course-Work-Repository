import serial
import time

seri= serial.Serial('/dev/ttyACM0',4800,timeout=10)


while True:
	read_ser=seri.read(1)
	print read_ser
	time.sleep(1)
	
seri.close()