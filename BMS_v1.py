
import serial
import crc8_dallas as crc8


class BMS(self):
	#variables:
	#connection (ser)
	def __init__(self, PORT, BAUDRATE):
		self.ser = serial.Serial(port=PORT, baudrate=BAUDRATE,bytesize=8,parity='N',xonxoff=0)
	def VR1(self):
		"""
			Returns the hardware type, serial number, and firmware version.
		"""
		sentence = "VR1,?,"
		number = crc8(sentence)
		sentence += str(number)
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "VR1"
		#r[1]: hardware type
		#r[2]: serial number
		#r[3]: firmware virstion
		return [("hardware type: " + r[1]), ("serial number: " + r[2]),
		("firmware version: " + r[3])]
	def BB1(self):
		sentence = "BB1,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BB1"
		
		if r[1] == '':
			#EMUS BMS control unit cannot communicate to cells.
			print("BMS cannot communicate to the cells.")
			return []
		else:
			numberOfCells = int(r[1])
			minCellBalancingRate = int(r[2],16)*100/255
			maxCellBalancingRate = int(r[3],16)*100/255
			averageCellBalancingRate = int(r[3],16)*100/255
			#r[4] is always empty
			balancingVoltageThreshold = (int(r[4],16)+200)*0.01
			return [numberOfCells,minCellBalancingRate,maxCellBalancingRate,averageCellBalancingRate,balancingVoltageThreshold]
	def BB2(self):
		sentence = "BB2,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BB2"
		
		if r[1] == '':
			#EMUS BMS control unit cannot communicate to cells.
			print("BMS cannot communicate to the cells.")
			return []
		else:
			cellStringNumber = int(r[1],16)
			firstCellNumber = int(r[2],16)
			sizeOfGroup = int(r[3],16)
			individualCellModuleBalancingRate = int(r[4],16)*100/255
			for x in range(sizeOfGroup):
				response = self.ser.readline()
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BB2"
			return [cellStringNumber,firstCellNumber,sizeOfGroup,individualCellModuleBalancingRate]	
				
				
greenhouseBMS = BMS("COM1", 57600)		
print(greenhouseBMS.VR1())