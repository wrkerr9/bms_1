#imports
from crc8_dallas import calcCheckSum as crc8
import serial
# this is a FT232R USB port





#serial commands
def sendRequest(sentence, ser):
	"""
	sends a request. Easy to change to Bluetooth if required.
	
	@argument sentence: must be a string. Hopefully it's formatted 
	properly.
	@argument ser: must be a serial port already opened.
	
	@return: nothing.
	"""
	if not ser.is_open:
		return -1
	sendingData = bytearray(sentence, "ascii")
	
	ser.write(sendingData)
def getResponse(ser):
	"""
	reads a response. Easy to change to bluetooth if required:
	@argument ser: must be a serial port already opened.
	@return: 1 sentence.
	"""
	if not ser.is_open:
		return -1
	return ser.readline()
#BMS com mands

def BB1(ser):
	""" 
	Requests data for Battery Balancing Rate Summary Sentence
	@argument ser: the serial port used.
	@return:  Array of Numbers, denoted as a.
	a[0] = number of cells, 
	a[1] = min_cell_balancing_rate 
	a[2] = max cell balancing rate
	a[3] = average cell balancing rate
	a[4] = balancing voltage threshold. 

	If the BMS cannot communicate with cells, array is empty.	
	"""
	#send the BMS a request for BB1.
	sentence = "BB1,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	sendRequest(sentenceRequest, ser)
	
	#read one sentence from the BMS.
	sentenceResponse = getResponse(ser)
	assert crc8(sentenceResponse[:2]) == int(sentenceResponse[-2:]) # crc check
	data = sentenceResponse.split(',')
	assert data[0] == "BB1" #Check if it's the right sentence.
	numberOfCells = data[1]
	min_cell_balancing_rate = data[2]*100/255
	max_cell_balancing_rate = data[3]*100/255
	average_cell_balancing_rate = data[4]*100/255
	balancing_voltage_threshold = data[6]*0.01
	
	return [numberOfCells, min_cell_balancing_rate,max_cell_balancing_rate,average_cell_balancing_rate,
	balancing_voltage_threshold]
	
def BB2(ser):
	#send a request to the BMS for Battery Balancing data.
	sentence = "BB2,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	sendRequest(sentenceRequest,ser)
	
	#receive a response from the BMS containing Battery Balancing data.
	#we need to read X sentences, where X is the size of the group.
	#do while loops don't exist in python.
	a = 1
	limit = 2
	result = []
	while a < limit:
		sentenceResponse = getResponse(ser)
		assert crc8(sentenceResponse[:2]) == int(sentenceResponse[-2:]) # crc check
		data = sentenceResponse.split(',')
		assert data[0] == "BB2" #Check if it's the right sentence.
		#these are all HexDec numbers.
		#the number is in hexadecimal.
		#no offset or multiplier here, but if there was:
		#value = (decimal(DATA) + offset)*multiplier
		cellStringNumber = int(data[1],16)
		cellNumber = int(data[2],16)
		sizeOfGroup = int(data[3],16)
		#this is a HexDecByteArray.
		#This always has an even number of entries.
		#each entry is 1 byte.
		
		offset = 0
		multiplier = 100.0/255.0
		for byte in data[4]:
			print(byte)
		
		individualCellModuleBalancingRate = int(data[4],16)*100/255
		
		
		
		result += [cellStringNumber,cellNumber,sizeOfGroup,individualCellModuleBalancingRate]
		if sizeOfGroup > (limit + 1):
			limit = sizeOfGroup + 1
		a += 1
	return result
	
def BC1(ser):
	#request Battery Charge Data
	sentence = "BC1,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	sendRequest(sentenceRequest,ser)
	
	#receive battery charge daa.
	sentenceResponse = getResponse(ser)
	assert crc8(sentenceResponse[:2]) == int(sentenceResponse[-2:]) #crc check.
	data = sentenceResponse.split(',')
	assert data[0] == "BC1" #Check if it's the right sentence.
	
	#Process data.
	#all of these are HexDec value.
	#they come in hex strings. Process it like this:
	#
	battery_charge = int(data[1],16)
	battery_capacity = int(data[2],16) # in Coulombs
	state_of_charge = data[3]*0.01
	return [battery_charge,battery_capacity,state_of_charge]
	
def BT1(ser):
	#Request BAttery Cell Module Temperature Data.
	sentence = "BT1,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	sendRequest(sentenceRequest, ser)
	
	#Receive data
	sentenceResponse = getResponse(ser)
	assert crc8(sentenceResponse[:2]) == int(sentenceResponse[-2:]) #crc check.
	data = sentenceResponse.split(',')
	assert data[0] == "BT1" #Check if it's the right sentence.
	
	#Process data.
	number_of_cells  = data[1] - 100
	min_cell_module_temp = data[2] - 100
	max_cell_module_temp = data[3] - 100
	average_cell_module_temp = data[4] - 100
	
	return [number_of_cells,min_cell_module_temp, max_cell_module_temp, average_cell_module_temp]	
def BT2():
	sentence = "BT2,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	print(sentenceRequest)
def BT3():
	sentence = "BT3,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	print(sentenceRequest)
def BT4():
	sentence = "BT4,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	print(sentenceRequest)
def BV1():
	sentence = "BV1,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	print(sentenceRequest)
def BV2():
	sentence = "BV2,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	print(sentenceRequest)
"""def CF2():
def CG1():
def CN1():
def CN2():
def CS1():
def CS2():
def CS3():
def CS4():
def CV1():
def DT1():
def FD1():
def IN1():
def LG1():
def OT1():
def PW1():
def PW2():
def RC1():
def RS1():
def RS2():
def SC1():
def SS1():
def ST1():
def TD1():
def TC1():
def TC2():"""
def VR1(ser):
	sentence = "VR1,?,"
	checksum = crc8(sentence)
	sentenceRequest = sentence + str(format(checksum,'x'))
	print(sentenceRequest)
	sendRequest(sentenceRequest,ser)
	
	sentenceResponse = getResponse(ser)
	assert crc8(sentenceResponse[:2]) == int(sentenceResponse[-2:],16) #crc check.
	data = sentenceResponse.split(',')
	assert data[0] == "VR1" #Check if it's the right sentence. 
	hardware_type = data[1]
	serial_number = int(data[2],16)
	firmware_version = data[3]
	print("Hardware type:", hardware_type)
	print("Serial Number:", serial_number)
	print("Firmware Version:", firmware_version)