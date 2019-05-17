import serial #to get this, run command pip install pyserial
from serial import SerialException
import io
import sys
from bmsrequest import *
	
BAUD = 57600 #57.6kbps = 
DATA_BITS = 8
PARITY = 0
STOP_BITS = 1
HARDWARE_FLOW_CONTROL = 0



#testing COM5
ports = []
if sys.platform.startswith('win'):
	ports = ['COM%s' % (i+1) for i in range(256)]
elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
	ports = glob.glob('/dev/ttyUSB*')
elif sys.platform.startswith('darwin'):
	ports = glob.glob('/dev/tty.usbserial*')
else:
	raise EnvironmentError('Error finding ports on your operating system')
openbci_port = ''
# test every port found
for port in ports: 
	try:
		s = serial.Serial(port= port, baudrate = BAUD)
		openbci_port = port
		s.close()
	except (OSError, serial.SerialException):
		pass
		
try:
	ser = serial.Serial()
	ser.baudrate = BAUD
	ser.port = openbci_port
	ser.open()
	print(ser.is_open)
	print(ser.name) #print what port was reallly opened.
	print(ser.readline())
	VR1(ser)
	ser.close()
except SerialException:
	print(SerialException)
	print(SerialException.errno)
	print(SerialException.message)


