import serial
import time
ser = serial.Serial('/dev/ttyAMA0',4800)
s="Hello from pi.Over to galileo"
while True:
	ser.write(s)
