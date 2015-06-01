import serial # if you have not already done so
ser = serial.Serial('/dev/tty.usbserial', 9600)
ser.write('5')
