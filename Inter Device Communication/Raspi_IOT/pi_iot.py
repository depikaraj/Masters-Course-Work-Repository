# Import all the libraries we need to run
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import Adafruit_DHT
import urllib2



DEBUG = 1
# Setup the pins we are connect to
DHTpin = 23

#Setup our API and delay
myAPI = "SRUBMNT7IMAFPA1Y"
myDelay = 15 #how many seconds between posting data

GPIO.setmode(GPIO.BCM)#use board numbering

def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)
    
    #Convert from Celius to Farenheit
    TWF = 1.8*TW+32
    
    # return dict
    return (str(RHW), str(TW),str(TWF))


# main() function
def main():
    
    print 'starting...dht11 is connected to the pi.Reading temperature and humidity data'

    baseURL ='https://api.thingspeak.com/update?api_key=%s' % myAPI
    print baseURL
    
    while True:
        try:
            RHW, TW, TWF = getSensorData()
          
            f = urllib2.urlopen(baseURL +"&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW))
            print f.read()
	    print "temp-c temp-f humidity"
            print TW + " " + TWF+ " " + RHW 
            f.close()
            

            sleep(int(myDelay))
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()

