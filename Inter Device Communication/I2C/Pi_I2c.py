import smbus
import time
# for RPI version 1, use bus = smbus.SMBus(0)
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x05

def writechar(value):
	bus.write_byte(address, value)
# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
# number = bus.read_byte_data(address, 1)
	return number

while True:
	var = raw_input("Enter your message:")
	
	if not var:
		continue
	for c in var:
		
		writechar(ord(c))
	print "RPI: Hi Arduino, I sent you ", var
# sleep one second
	time.sleep(1)

# 	number = readNumber()
# print "Arduino: Hey RPI, I received a digit ", number