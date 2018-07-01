#Created by MF ALFAFA
#1 July 2018
#miftahf77@gmail.com

import serial

connected = False
ser = 0
x=0

## Establish connection to COM Port
locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3','COM8']

for device in locations:
    try:
        print "Trying...",device
        ## Serial Initialization
        ser = serial.Serial(device,             #port
                            19200,              #baudrate
                            serial.EIGHTBITS,   #bytesize
                            serial.PARITY_ODD,  #parity
                            serial.STOPBITS_ONE,#stop bit
                            None,               #timeout
                            False,              #xonxoff
                            False,              #rtscts
                            None,               #write_timeout
                            False,              #dsrdtr
                            None,               #inter byte timeout
                            None                #exclusive
                            )
        break
    except:
        print "Failed to connect on ", device

## loop until the device tells us it is ready
while not connected:
    serin = ser.read()
    connected = True

## open text file to store the current    
text_file = open("serial_data.txt", 'w')
## write it to the text file 'serial_data.txt'
while 1:
    if ser.inWaiting(): #waiting for incoming serial data
        x=ser.read()
        text_file.write(x)
        if x=="\n":
             text_file.seek(0)
             text_file.truncate()
        text_file.flush()
        print x
    #print(x)

## close the serial connection and text file
text_file.close()
ser.close()
