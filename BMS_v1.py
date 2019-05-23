
import serial
import crc8_dallas as crc8

class BMSstatistic(self):
	"""
		used in the sentence SS1
	"""
	unit = 'N/A'
	def __init__(self,statisticIdentifier,statisticValue,statisticValueAdditionalInfo,timestamp):
		self.statisticIdentifier = statisticIdentifier
		self.statisticValue = statisticValue
		self.statisticValueAdditionalInfo = statisticValueAdditionalInfo
		self.timestamp = timestamp + 946684800
		s1 = statisticIdentifier
		if s1 == 0:	self.totalDischarge()
		if s1 == 1: self.totalCharge()
		if s1 == 2: self.totalDischargeEnergy()
		if s1 == 3: self.totalChargeEnergy()
		if s1 == 4: self.totalDischargeTime()
		if s1 == 5: self.totalChargeTime()
		if s1 == 6: self.totalDistance()
		if s1 == 7: self.masterClearCount()
		if s1 == 8: self.maxDischargeCurrent()
		if s1 == 9: self.maxChargeCurrent()
		if s1 == 10: self.minCellVoltage()
		if s1 == 11: self.maxCellVoltage()
		if s1 == 12: self.maxCellVoltageDifference()
		if s1 == 13: self.minPackVoltage()
		if s1 == 14: self.maxPackVoltage()
		if s1 == 15: self.minCellModuleTemperature()
		if s1 == 16: self.maxCellModuleTemperature()
		if s1 == 17: self.maxCellModuleTemperatureDifference()
		if s1 == 18: self.BMS_starts_count()
		if s1 == 19: self.undervoltage_protection_count()
		if s1 == 20: self.overvoltage_protection_count()
		if s1 == 21: self.discharge_overcurrent_protection_count()
		if s1 == 22: self.charge_overcurrent_protection_count()
		if s1 == 23: self.cell_module_overheat_protection_count()
		if s1 == 24: self.leakage_protection_count()
		if s1 == 25: self.no_cell_comm_protection_count()
		if s1 == 26: self.low_voltage_power_reduction_count()
		if s1 == 27: self.high_current_power_reduction_count()
		if s1 == 28: self.high_cell_module_temperature_power_reduction_count()
		if s1 == 29: self.charger_connect_count()
		if s1 == 30: self.charger_disconnect_count()
		if s1 == 31: self.preheat_stage_count()
		if s1 == 32: self.precharge_stage_count()
		if s1 == 33: self.main_charge_stage_count()
		if s1 == 34: self.balancing_stage_count()
		if s1 == 35: self.charging_finished_count()
		if s1 == 36: self.charging_error_occurred_count()
		if s1 == 37: self.charging_retry_count()
		if s1 == 38: self.trips_count()
		if s1 == 39: self.charge_restarts_count()
		if s1 == 45: self.cell_overheat_protection_count()
		if s1 == 46: self.high_cell_module_temperature_power_reduction_count()
		if s1 == 47: self.min_cell_temperature()
		if s1 == 48: self.max_cell_temperature()
		if s1 == 49: self.max_cell_temperature_difference()
	def totalDischarge(self):
		self.unit = 'Ah'
	def totalCharge(self):
		self.unit = 'Ah'
	def totalDischargeEnergy(self):
		self.unit = 'Wh'
	def totalChargeEnergy(self):
		self.unit = 'Wh'
	def totalDischargeTime(self):
		self.unit = 's'
	def totalChargeTime(self):
		self.unit = 's'
	def totalDistance(self):
		self.unit = 'pulses'
	def masterClearCount(self):
		self.name = 'count'
	def maxDischargeCurrent(self):
		self.unit = 'A'
		self.statisticValue *= 0.1
	def maxChargeCurrent(self):
		self.unit = 'A'
		self.statisticValue *= 0.1
	def minCellVoltage(self):
		self.unit = 'V'
		self.statisticValue = (self.statisticValue + 200) * 0.1
		self.additional_info_meta = 'Cell ID'
	def maxCellVoltage(self)
		self.unit = 'V'
		self.statisticValue = (self.statisticValue + 200) * 0.1
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellVoltageDifference(self):
		self.unit = 'V'
		self.statisticValue = (self.statisticValue) * 0.1
		bytemap = hex(self.statisticValueAdditionalInfo)[2:].upper()
		
		self.min_cell_voltage = (int(bytemap[0],16) + 200) * 0.1
		self.max_cell_voltage = (int(bytemap[1],16) ) * 0.1
		self.cell_ID = int(bytemap[2:3],16)
		"""
		LSB - Min cell voltage at the time
		max cell voltage difference was registerd.
		"""
	def minPackVoltage(self):
		self.unit = 'V'
		self.statisticValue *= 0.1
	def maxPackVoltage(self):
		self.unit = 'V'
		self.statisticValue *= 0.1
	def minCellModuleTemperature(self):
		self.unit = 'C'
		self.statisticValue = self.statisticValue - 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellModuleTemperature(self):
		self.unit = 'C'
		self.statisticValue = self.statisticValue - 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellModuleTemperatureDifference(self):
		self.unit = 'C'
		bytemap = hex(self.statisticValueAdditionalInfo)[2:].upper()
		
		self.min_cell_voltage = (int(bytemap[0],16) -100)
		self.max_cell_voltage = (int(bytemap[1],16) -100)
		self.cell_ID = int(bytemap[2:3],16)
	def BMS_starts_count(self):
		self.unit = 'N/A'
	def undervoltage_protection_count(self):
		self.unit = 'N/A'
	def overvoltage_protection_count(self):
		self.unit = 'N/A'
	def discharge_overcurrent_protection_count(self):
		self.unit = 'N/A'
	def charge_overcurrent_protection_count(self):
		self.unit = 'N/A'
	def cell_module_overheat_protection_count(self):
		self.unit = 'N/A'
	def leakage_protection_count(self):
		self.unit = 'N/A'
	def no_cell_comm_protection_count(self):
		self.unit = 'N/A'
	def low_voltage_power_reduction_count(self):
		self.unit = 'N/A'
	def high_current_power_reduction_count(self):
		self.unit = 'N/A'
	def high_cell_module_temperature_power_reduction_count(self):
		self.unit = 'N/A'
	def charger_connect_count(self):
		self.unit = 'N/A'
	def charger_disconnect_count(self):
		self.unit = 'N/A'
	def preheat_stage_count(self):
		self.unit = 'N/A'
	def precharge_stage_count(self):
		self.unit = 'N/A'
	def main_charge_stage_count(self):
		self.unit = 'N/A'
	def balancing_stage_count(self):
		self.unit = 'N/A'
	def charging_finished_count(self):
		self.unit = 'N/A'
	def charging_error_occurred_count(self):
		self.unit = 'N/A'
	def charging_retry_count(self):
		self.unit = 'N/A'
	def trips_count(self):
		self.unit = 'N/A'
	def charge_restarts_count(self):
		self.unit = 'N/A'
	def cell_overheat_protection_count(self):
		self.unit = 'N/A'
	def high_cell_temperature_power_reduction_count(self):
		self.unit = 'N/A'
	def min_cell_temperature(self):
		self.unit = 'C'
		self.statistic -= 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def max_cell_temperature(self):
		self.unit = 'C'
		self.statistic -= 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def max_cell_temperature_difference(self):
		self.unit = 'C'
		bytemap = hex(self.statisticValueAdditionalInfo)[2:].upper()
		self.min_cell_temperature = int(bytemap[0],16) - 100
		self.max_cell_temperature = int(bytemap[1],16) - 100
		self.cell_ID = int(bytemap[2:3],16)
		
class BMS(self):
	#variables:
	y2kInEpoch = 946684800
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
			cellGroups = []
			cellStringNumber = int(r[1],16)
			firstCellNumber = int(r[2],16)
			sizeOfGroup = int(r[3],16)
			individualCellModuleBalancingRate = int(r[4],16)*100/255
			cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellModuleBalancingRate])
			for x in range(sizeOfGroup):
				response = self.ser.readline()
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BB2"
				cellStringNumber = int(r[1],16)
				firstCellNumber = int(r[2],16)
				sizeOfGroup = int(r[3],16)
				individualCellModuleBalancingRate = int(r[4],16)*100/255
				cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellModuleBalancingRate])
			return cellGroups
	def BC1(self):
		sentence = "BC1,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BC1"
	def BT1(self):
		"""
		summary of cell module temperature values.
		
		
		"""
		sentence = "BT1,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT1"
		if r[1] == '':
			return []
		else:	
			numberOfCells = int(r[1],16)
			minCellModuleTemp = int(r[2],16) - 100
			maxCellModuleTemp = int(r[3],16) - 100
			averageCellModuleTemp = int(r[4],16) - 100
			
			
			return [numberOfCells,minCellModuleTemp,maxCellModuleTemp,averageCellModuleTemp]
	def BT2(self):
		sentence = "BT2,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT2"
		if r[1] == '':
			return []
		else:
			cellGroups = []
			cellStringNumber = int(r[1],16)
			firstCellNumber = int(r[2],16)
			limit = int(r[3],16)
			sizeOfGroup = limit
			individualCellModuleTemperatures = int(r[4,16)-100)
			cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellModuleTemperatures])
			for i in range(limit-1):
				response = self.ser.readline()
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BT2"
				cellStringNumber = int(r[1],16)
				firstCellNumber = int(r[2],16)
				limit = int(r[3],16)
				sizeOfGroup = limit
				individualCellModuleTemperatures = int(r[4,16)-100)
				cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellModuleTemperatures])
			return cellGroups
	def BT3(self):
		sentence = "BT3,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT3"
		
		if r[1] == '':
			return []
		else:
			numberOfCells = int(r[1],16)
			minCellTemp = int(r[2],16) - 100
			maxCellTemp = int(r[3],16) - 100
			averageCellTemp = int(r[4],16) - 100
			return [numberOfCells,minCellTemp,maxCellTemp,averageCellTemp]
	def BT4(self):
		sentence = "BT4,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT4"
		
		if r[1] == '':
			return []
		else:
			cellGroups = []
			cellStringNumber = int(r[1],16)
			firstCellNumber = int(r[2],16)
			limit = int(r[3],16)
			sizeOfGroup = limit
			individualCellTemperatures = int(r[4,16)-100)
			cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellTemperatures])
			for i in range(limit-1):
				response = self.ser.readline()
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BT2"
				cellStringNumber = int(r[1],16)
				firstCellNumber = int(r[2],16)
				limit = int(r[3],16)
				sizeOfGroup = limit
				individualCellTemperatures = int(r[4,16)-100)
				cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellTemperatures])
			return cellGroups
	def BV1(self):
		sentence = "BV1,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BV1"
		
		if r[1] == '':
			return []
		else:
			numberOfCells = int(r[1],16)
			minCellVoltage = (int(r[2],16) + 200 ) * 0.01
			maxCellVoltage = (int(r[3],16) + 200 ) * 0.01
			averageCellVoltage = (int(r[4],16) + 200 ) * 0.01
			totalVoltage = (int(r[2],16) ) * 0.01
			return [numberOfCells,minCellVoltage,maxCellVoltage,averageCellVoltage,totalVoltage]
	def BV2(self):
		sentence = "BV2,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BV2"
		
		if r[1] == '':
			return []
		else:
			cellGroups = []
			cellStringNumber = int(r[1],16)
			firstCellNumber = int(r[2],16)
			limit = int(r[3],16)
			sizeOfGroup = limit
			individualCellVoltages = (int(r[4,16)+200)*0.01
			cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellVoltages])
			for i in range(limit-1):
				response = self.ser.readline()
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BT2"
				cellStringNumber = int(r[1],16)
				firstCellNumber = int(r[2],16)
				limit = int(r[3],16)
				sizeOfGroup = limit
				individualCellVoltages = (int(r[4,16)+200)*0.01
				cellGroups.append([cellStringNumber,firstCellNumber,sizeOfGroup,individualCellVoltages])
			return cellGroups
	def CF2(self, parameterID):
		"""
		parameterID must be an integer.
		
		returns the parameter. Must be processed separately.
		"""
		sentence = "CF2," + str(parameterID.hex()) + ",?"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CF2"
		assert r[1] == str(parameterID.hex())
		return int(r[2],16)
	def CN1(self)	
		"""
		reports the CAN messages received on CAN bus is "Send to RS232/USB function is enabled.
		
		"""
		sentence = "CN1,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CN1"
		CANIdentifier = int(r[1],16)
		identifierExtensionFlag = True if r[2] == '1' else False
		remoteTransmissinoRequestFlag = True if r[3] == '1' else False
		dataLength = int(r[4],10)
		data = [r[5][i:i+2] for i in range(0,len(r[5]),2)]
		return [CANIdentifier,identifierExtensionFlag,remoteTransmissinoRequestFlag,dataLength,data]
	def CN2(self):
		"""
		reports the CAN messages sent on CAN bus if "Send to RS232/USB function is enabled.
		"""
		sentence = "CN2,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CN2"
		CANIdentifier = int(r[1],16)
		identifierExtensionFlag = True if r[2] == '1' else False
		remoteTransmissinoRequestFlag = True if r[3] == '1' else False
		dataLength = int(r[4],10)
		data = [r[5][i:i+2] for i in range(0,len(r[5]),2)]
		return [CANIdentifier,identifierExtensionFlag,remoteTransmissinoRequestFlag,dataLength,data]
	def CS1(self):
		"""
			contains the parameters and status of the charger.
			
		"""
		sentence = "CS1,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CS1"
		numberOfConnectedChargers = int(r[1],16)
		CANChargerStatus = int(r[2],16)
		setVoltage = int(r[3],16)*0.1
		setCurrent = int(r[4],16)*0.1
		actualVoltage = int(r[5],16)*0.1
		actualCurrent = int(r[6],16)*0.1
		return [numberOfConnectedChargers,CANChargerStatus,setVoltage,setCurrent,actualVoltage,actualCurrent]
	def CV1(self):
		"""
			contains the values of total voltage of battery pack,
			and current flowing through the battery pack.
		"""
		sentence = "CV1,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CV1"
		totalVoltage = int(r[1],16)*0.01
		current = int(r[2],16)*0.1
		return [totalVoltage,Current]
	def DT1(self):
		""" This is a placeholder for an electric vehicle sentence.
		This is being programmed for a greenhouse, so this will not
		be programmed for.
		"""
		return []
	def FD1(self):
		"""
			This function resets the unit to factory defaults. Use at your own risk.
		"""
		sentence = "FD1,,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		return
	def IN1(self):
		"""
			Input Pins status.
			AC Sense plugged in,
			IGN. In plugged in,
			Fast Chg plugged in.
		"""
		sentence = "IN1,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "IN1"
		bitField = int(r[1],16)
		AC_SENSE = True if (bitField & 0x08) else False 
		IGN_IN  = True if (bitField & 0x10) else False 
		FAST_CHG = True if (bitField & 0x20) else False
		return [AC_SENSE,IGN_IN, FAST_CHG]
	def LG1(self, clear='N'):
		"""
			Retrieve events logged.
			To clear the event logger, pass in a 'C', like
			BMS.LG1('C')
			
		"""
		sentence = "LG1,"
		if clear == 'C':
			sentence += 'c,'
		else:
			sentence += '?,'
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "LG1"
		logEventDictionary = {	0: 'No event',
								1: 'BMS Started',
								2: 'Lost Communication to Cells',
								3: 'Established communication to cells',
								4: 'Cells voltage critically low',
								5: 'Critical low voltage recovered',
								6: 'Cells voltage critically high',
								7: 'Critical high voltage recovered',
								8: 'Discharge Current critically high',
								9: 'Discharge cirtical high current recovered',
								10: 'Charge Current Critically high',
								11: 'Charge critical high current recovered',
								12: 'Cell module temperature critically high',
								13: 'Critical high cell module temperature recovered',
								14: 'Leakage detected',
								15: 'Leakage recovered',
								16: 'Warning: Low voltage - reducing power',
								17: 'Power reduction due to low voltage recovered',
								18: 'Warning: High current - reducing power',
								19: 'Power reduction due to high current recovered',
								20: 'Warning: High Cell module temperature - reducing power',
								21: 'Power reduction due to high cell module temperature recovered',
								22: 'Charger connected',
								23: 'Charger disconnected',
								24: 'Started pre-heating stage',
								25: 'Started pre-charging stage',
								26: 'Started main charging stage',
								27: 'Started Balancing stage',
								28: 'Charging finished',
								29: 'Charging error occurred',
								30: 'Retrying Chraging',
								31: 'Restarting Charging',
								42: 'Cell Temperature Critically High',
								43: 'Critically high cell temperature recovered',
								44: 'Warning: High cell temperature - reducing power'
							 }
		y2kTimestamp = int(r[4],16) #coded in seconds since January 1, 2000 time 00:00 (Y2K)
		#Unix epoch is January 1, 1970 00:00
		#add Y2K in epoch time 
		epochTimestamp = y2kTimestamp + self.y2kInEpoch 
		
		#convert epoch time stamp into a real class from the time library.
		import time
		timestamp = str(time.gmtime(epochTimestamp))
	
	def OT1(self):
		"""
			Returns status of output pins.
			[Charger pin, heater, bat. low, buzzer, chg. ind.]
		"""
		sentence = "OT1,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "OT1"
		CHARGER_PIN = True if (int(r[1],16) & 0x40) else False
		bitfield = int(r[3],16)
		HEATER = True if (bitfield & 0x08) else False
		BAT_LOW = True if (bitfield & 0x10) else False
		BUZZER = True if (bitfield & 0x20) else False
		CHG_IND = True if (bitfield & 0x40) else False 
		
		return [CHARGER_PIN,HEATER,BAT_LOW,BUZZER,CHG_IND]
	def PW1(self, request=None, password=None):
		"""
			Check the admin status with PW1('?').
			Log in to BMS system with PW1('P', password)
			Log out with PW1()
		"""
		sentence = "PW1,"
		if request == '?':
			sentence += "?,"
		elif request == 'P':
			sentence += str(password) + ","
		else:
			sentence += ","
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "PW1"
		
		authenticationCode = int(r[1],16)
		return authenticationCode
	def PW2(self, request, newPassword=None):
		"""
			Sets a new password, or clears a password.
			Set new password calling: PW2('S',"mynewpassword")
			Clear password: PW2('C')
			Returns true if successful, false if not successful.
		"""
		sentence = "PW2,"
		if request == 'C': #clear password
			sentence += ","
		elif request = 'S': #set a new password
			setence += str(newPassword) + ","
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		if r[0] == "PW2":
			setResult = int(r[1],16)
			return True if setResult == 1 else False
		else:
			return False
	def RC1(self):
		"""
			Resets the current sensor reading to zero. Used after current sensor is initially installed.
		"""
		sentence = "RC1,,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		return
	def RS1(self):
		"""
			Resets the Emus BMS control unit entirely. Like a sudo reboot on a
			linux machine.
		"""
		sentence = "RS1,,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		return
	def RS2(self):
		"""
			Retrieves the rest source history log.
		"""
		sentence = "RS2,?,"
		number = crc8(sentence)
		sentence += number
		self.ser.write(sentence)
		response = self.ser.readline()
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == 'RS2'
		records = []
		import time
		y2kInEpoch = time.gmtime(
		for i in range(1,10,2):
			timestamp =  int(r[i],16)+ self.y2kInEpoch
			timeStruct = time.gmtime(timestamp)
			resetSourceFlags = int(r[i+1],16)
			x = resetSourceFlags
			POWER_ON_RESET = True if x & 0x1 else False
			EXTERNAL_RESET = True if x & 0x2 else False
			BROWN_OUT_RESET = True if x & 0x4 else False
			WATCHDOG_RESET = True if x & 0x8 else False
			JTAG_REST = True if x & 0x10 else False
			STACK_OVERFLOW_RESET = True if x & 0x20 else False
			USER_CAUSED_RESET = True if x & 0x40 else False
			records.append(timestamp, [POWER_ON_RESET,EXTERNAL_RESET,BROWN_OUT_RESET,WATCHDOG_RESET,JTAG_REST,STACK_OVERFLOW_RESET,USER_CAUSED_RESET])
		return records
	def SC1(self, percentage):
		"""
		set the current state of the charge of the battery in %.
		send in an integer from 0 to 100.
		this method will convert to hexadecimal format first.
		returns False if not successful or invalid percentage is passed.
		returns True if successful.
		"""
		if not isinstance(percentage, int):
			return False
		elif (percentage < 0 or percentage > 100):
			return False
		else:
			sentence = "SC1," + hex(percentage)[2:].upper() + ","
			number = crc8(sentence)
			sentence += number
			self.ser.write(sentence)
			return True
	def SS1(self, request, statisticIdentifier=0):
		"""
		This method is used to retrive the statistics from the Emus BMS unit.
		request parameter:
		
		'?': request all statistics
		'N': request a numbered statistic. Pass in a number.
		'c': all unprotected statistics
		"""
		if request == '?':
			pass
		if request == 'N':
			if not isinstance(number, int):
				return -1
			sentence = "SS1," + hex(statisticIdentifier)[2:].upper() + ","
			number = crc8(sentence)
			sentence += number
			self.ser.write(sentence)
			response = self.ser.readline()
			assert crc8(response[:2]) == int(response[-2:]) # crc check
			r = response.split(',')
			assert r[0] == 'SS1'
			assert int(r[1],16) == statisticIdentifier
			statisticValue = int(r[2], 16)
			statisticValueAdditionalInfo = int(r[3],16)
			timeStamp = int(r[4],16)
			single_statistic = BMSstatistic(statisticValue,statisticValueAdditionalInfo,timeStamp)
			return single_statistic
			
	def	ST1(self):
		"""
			BMS Status sentence
		"""
		
greenhouseBMS = BMS("COM1", 57600)		
print(greenhouseBMS.VR1())