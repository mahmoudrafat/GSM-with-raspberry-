import serial
import os 
import time
# SMS Function
def send_text(number,text, path='/dev/ttyUSB0'):
        ser = serial.Serial(path, baudrate = 115200,  timeout=1)
        ser.write ('AT+CMGF=%d\r' % 1)
        time.sleep(1)
        ser.write ('AT+CSCS=%s\r' % "GSM")
        time.sleep(1)
        ser.write ('AT+CMGS="%s"\r' % number)
        time.sleep(1)
        ser.write ('%s\x1a' % text)
        time.sleep(1)
        print ser.readlines()
        print "done"
        time.sleep(2)
        print "done done"
        ser.close()
Send_text('00201xxxxxxxxx','Hello From Pi')        
