
import serial
import crc8_dallas as crc8


class BMSstatistic:
	"""
		used in the sentence SS1
	"""
	unit = 'N/A'
	def __init__(self,statisticIdentifier,statisticValue,statisticValueAdditionalInfo,timestamp):
		self.statisticIdentifier = statisticIdentifier
		self.statisticValue = statisticValue
		self.statisticValueAdditionalInfo = statisticValueAdditionalInfo
		self.timestamp = timestamp + 946684800 #the BMS for some reason records all their time relative to Jan 1, 2000. I'm converting it to the unix epoch time.
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
		self.name = 'Total Discharge'
		self.unit = 'Ah'
	def totalCharge(self):
		self.name = 'Total Charge'
		self.unit = 'Ah'
	def totalDischargeEnergy(self):
		self.name = 'Total Discharge Energy'
		self.unit = 'Wh'
	def totalChargeEnergy(self):
		self.name = 'Total Charge Energy'
		self.unit = 'Wh'
	def totalDischargeTime(self):
		self.name = 'Total Discharge Time'
		self.unit = 's'
	def totalChargeTime(self):
		self.name = 'Total Charge Time'
		self.unit = 's'
	def totalDistance(self):
		self.name = 'Total Distance'
		self.unit = 'pulses'
	def masterClearCount(self):
		self.name = 'Master Clear Count'
	def maxDischargeCurrent(self):
		self.name = 'Maximum Discharge Current'
		self.unit = 'A'
		self.statisticValue *= 0.1
	def maxChargeCurrent(self):
		self.name = 'Maximum Charge Current'
		self.unit = 'A'
		self.statisticValue *= 0.1
	def minCellVoltage(self):
		self.name = 'Minimum Cell Voltage'
		self.unit = 'V'
		self.statisticValue = (self.statisticValue + 200) * 0.1
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellVoltage(self):
		self.name = 'Maximum Cell Voltage'
		self.unit = 'V'
		self.statisticValue = (self.statisticValue + 200) * 0.1
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellVoltageDifference(self):
		self.name = 'Maximum Cell Voltage Difference'
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
		self.name = 'Minimum Pack Voltage'
		self.unit = 'V'
		self.statisticValue *= 0.1
	def maxPackVoltage(self):
		self.name = 'Maximum Pack Voltage'
		self.unit = 'V'
		self.statisticValue *= 0.1
	def minCellModuleTemperature(self):
		self.name = 'Minimum Cell Module Temperature'
		self.unit = 'C'
		self.statisticValue = self.statisticValue - 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellModuleTemperature(self):
		self.name = 'Maximum Cell Module Temperature'
		self.unit = 'C'
		self.statisticValue = self.statisticValue - 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def maxCellModuleTemperatureDifference(self):
		self.name = 'Maximum Cell Module Temperature Difference'
		self.unit = 'C'
		bytemap = hex(self.statisticValueAdditionalInfo)[2:].upper()
		
		self.min_cell_voltage = (int(bytemap[0],16) -100)
		self.max_cell_voltage = (int(bytemap[1],16) -100)
		self.cell_ID = int(bytemap[2:3],16)
	def BMS_starts_count(self):
		self.name = 'BMS Starts Count'
		self.unit = 'N/A'
	def undervoltage_protection_count(self):
		self.name = 'Under-voltage protection count'
		self.unit = 'N/A'
	def overvoltage_protection_count(self):
		self.name = 'Over-voltage protection count'
		self.unit = 'N/A'
	def discharge_overcurrent_protection_count(self):
		self.name = 'Discharge over-current protection count'
		self.unit = 'N/A'
	def charge_overcurrent_protection_count(self):
		self.name = 'Charge over-current protection count'
		self.unit = 'N/A'
	def cell_module_overheat_protection_count(self):
		self.name = 'Cell module overheat protection count'
		self.unit = 'N/A'
	def leakage_protection_count(self):
		self.name = 'Leakage protection count'
		self.unit = 'N/A'
	def no_cell_comm_protection_count(self):
		self.name = 'No cell communication protection count'
		self.unit = 'N/A'
	def low_voltage_power_reduction_count(self):
		self.name = 'Low Voltage Power Reduction Count'
		self.unit = 'N/A'
	def high_current_power_reduction_count(self):
		self.name = 'High Current Power Reduction Count'
		self.unit = 'N/A'
	def high_cell_module_temperature_power_reduction_count(self):
		self.name = 'High Cell Module Temperature Power Reduction Count'
		self.unit = 'N/A'
	def charger_connect_count(self):
		self.name = 'Charger Connect Count'
		self.unit = 'N/A'
	def charger_disconnect_count(self):
		self.name = 'Charger Disconnect Count'
		self.unit = 'N/A'
	def preheat_stage_count(self):
		self.name = 'Preheat Stage Count'
		self.unit = 'N/A'
	def precharge_stage_count(self):
		self.name = 'Precharge Stage Count'
		self.unit = 'N/A'
	def main_charge_stage_count(self):
		self.name = 'Main Charge Stage Count'
		self.unit = 'N/A'
	def balancing_stage_count(self):
		self.name = 'Balancing Stage Count'
		self.unit = 'N/A'
	def charging_finished_count(self):
		self.name = 'Charging Finished Count'
		self.unit = 'N/A'
	def charging_error_occurred_count(self):
		self.name = 'Charging Error Occurred Count'
		self.unit = 'N/A'
	def charging_retry_count(self):
		self.name = 'Charging Retry Count'
		self.unit = 'N/A'
	def trips_count(self):
		self.name = 'Trips Count'
		self.unit = 'N/A'
	def charge_restarts_count(self):
		self.name = 'Charging Restarts Count'
		self.unit = 'N/A'
	def cell_overheat_protection_count(self):
		self.name = 'Cell Overheat Protection Count'
		self.unit = 'N/A'
	def high_cell_temperature_power_reduction_count(self):
		self.name = 'High Cell Temperature power reduction count'
		self.unit = 'N/A'
	def min_cell_temperature(self):
		self.name = 'Minimum Cell Temperature'
		self.unit = 'C'
		self.statisticValue -= 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def max_cell_temperature(self):
		self.name = 'Maximum Cell Temperature'
		self.unit = 'C'
		self.statisticValue -= 100
		self.cell_ID = self.statisticValueAdditionalInfo
	def max_cell_temperature_difference(self):
		self.name = 'Maximum Cell Temperature Difference'
		self.unit = 'C'
		bytemap = hex(self.statisticValueAdditionalInfo)[2:].upper()
		self.min_cell_temperature = int(bytemap[0],16) - 100
		self.max_cell_temperature = int(bytemap[1],16) - 100
		self.cell_ID = int(bytemap[2:3],16)
	def __str__(self):
		"""
		{
			name: Name, 
			value: Value,
			unit: Unit,
			time: Time Recorded in Unix Epoch Time
			min_cell_temperature: Min cell_temperature
			max_cell_temperature: Max cell_temperature
			cell ID: Cell_ID
		}
		"""
		string = "{"
		
		if hasattr(self, 'name'):
			string += '"name":"' + self.name + '",'
		if hasattr(self, 'statisticValue'):
			string += '"value":"' + str(self.statisticValue) + '",'
		if hasattr(self, 'unit'):
			string += '"unit":"' + str(self.unit) + '",'
		if hasattr(self, 'timestamp'):
			string += '"time":' + str(self.timestamp) + '",'
		if hasattr(self, 'min_cell_temperature'):
			string += '"minimum cell temperature":' + str(self.min_cell_temperature) + '",'
		if hasattr(self, 'max_cell_temperature'):
			string += '"maximum cell temperature":' + str(self.max_cell_temperature) + '",'
		if hasattr(self, 'cell_ID'):
			string += '"Cell ID":' + str(self.cell_ID) + '",'
		
		string += "}"
		
		return string
	def dict(self)
		varDict = {}
		if hasattr(self, 'name'):
			varDict['name'] = self.name
		if hasattr(self, 'statisticValue'):
			varDict['value'] = self.value
		if hasattr(self, 'unit'):
			varDict['unit'] = self.unit
		if hasattr(self, 'timestamp'):
			varDict['timestamp'] = self.timestamp
		if hasattr(self, 'min_cell_temperature'):
			varDict['minimum cell temperature'] = self.min_cell_temperature
		if hasattr(self, 'max_cell_temperature'):
			varDict['maximum cell temperature'] = self.max_cell_temperature
		if hasattr(self, 'cell_ID'):
			varDict['Cell ID'] = self.cell_ID
		return varDict
class BMS:
	#variables:
	y2kInEpoch = 946684800
	#connection (ser)
	def __init__(self, PORT, BAUDRATE):
		self.ser = serial.Serial(port=PORT, baudrate=BAUDRATE,bytesize=8,parity='N',xonxoff=0)
	def execute(self, sentence):
		byteArray = bytes(sentence, 'ascii')
		self.ser.write(byteArray)
	def VR1(self):
		"""
			Returns a dictionary of the hardware type, serial number, and firmware version.
		"""
		sentence = "VR1,?,"
		number = crc8(sentence)
		sentence += str(number)
		self.execute(sentence)
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "VR1"
		#r[1]: hardware type
		#r[2]: serial number
		#r[3]: firmware version
		data = {}
		data['hardware type'] = r[1]
		data['serial number'] = r[2]
		data['firmware version'] = r[3]
		return data

	def BB1(self):
		sentence = "BB1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BB1"
		
		if r[1] == '':
			#EMUS BMS control unit cannot communicate to cells.
			print("BMS cannot communicate to the cells.")
			return {"BMS cannot communicate to the cells."}
		else:
			numberOfCells = int(r[1])
			minCellBalancingRate = int(r[2],16)*100/255
			maxCellBalancingRate = int(r[3],16)*100/255
			averageCellBalancingRate = int(r[3],16)*100/255
			#r[4] is always empty
			balancingVoltageThreshold = (int(r[4],16)+200)*0.01
			data = {}
			data['number of cells'] = numberOfCells
			data['minimum cell balancing rate'] = minCellBalancingRate
			data['maximum cell balancing rate'] = maxCellBalancingRate
			data['average cell balancing rate'] = averageCellBalancingRate
			data['balancing voltage threshold'] = balancingVoltageThreshold
			return data
			#return [numberOfCells,minCellBalancingRate,maxCellBalancingRate,averageCellBalancingRate,balancingVoltageThreshold]
	def BB2(self):
		sentence = "BB2,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BB2"
		
		if r[1] == '':
			#EMUS BMS control unit cannot communicate to cells.
			print("BMS cannot communicate to the cells.")
			return {"BMS cannot communicate to the cells."}
		else:
			data = {}
			cellGroups = []
			cellStringNumber = int(r[1],16)
			firstCellNumber = int(r[2],16)
			sizeOfGroup = int(r[3],16)
			individualCellModuleBalancingRate = int(r[4],16)*100/255
			cell_group_1 = {}
			cell_group_1['cell string number'] = cellStringNumber
			cell_group_1['first cell number'] = firstCellNumber
			cell_group_1['size of group'] = sizeOfGroup
			cell_group_1['individual cell module balancing rage'] = individualCellModuleBalancingRate
			data['cell group 1'] = cell_group_1
			for x in range(sizeOfGroup-1):
				response = self.ser.readline().decode('ascii')
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BB2"
				
				cellStringNumber = int(r[1],16)
				firstCellNumber = int(r[2],16)
				sizeOfGroup = int(r[3],16)
				individualCellModuleBalancingRate = int(r[4],16)*100/255
				cell_group_x = {}
				cell_group_x['cell string number'] = cellStringNumber
				cell_group_x['first cell number'] = firstCellNumber
				cell_group_x['size of group'] = sizeOfGroup
				cell_group_x['individual cell module balancing rage'] = individualCellModuleBalancingRate
				data['cell group ' + str(x+2)] = cell_group_x
			return data

	def BC1(self):
		sentence = "BC1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BC1"
		data = {}
		data['battery charge'] = int(r[1],16)
		data['battery capacity'] = int(r[2],16)
		data['state of charge'] = int(r[3],16)*0.01
		return data
	def BT1(self):
		"""
		Battery Cell Module Temperature Summary Sentence
		This sentence contains the summary of cell module temperature values of the battery pack.
		
		"""
		sentence = "BT1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
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
			data = {}
			data['number of cells'] = numberOfCells
			data['minimum cell module temperature'] = minCellModuleTemp
			data['maximum cell module temperature'] = maxCellModuleTemp
			data['average cell module temperature'] = averageCellModuleTemp
			return data
			
			#return [numberOfCells,minCellModuleTemp,maxCellModuleTemp,averageCellModuleTemp]
	def BT2(self):
		"""
			Battery Cell Module Temperature Detail Sentence
			
			This sentence contains individual cell module temperatures of a group of cells. Each group consists of 1 to 8 cells. This sentence is sent only after Control Unit receives a request sentence from external device, where the only data field is ‘?’ symbol. The normal response to BT2 request message, when battery pack is made up of two parallel cell strings:

		"""
		sentence = "BT2,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT2"
		if r[1] == '':
			return {"Cells cannot be communicated to."}
		else:
			data = {}
			cell_group_1 = {}
			cell_group_1['cell string number'] = int(r[1],16)
			cell_group_1['cell number of first cell in group'] = int(r[2],16)
			cell_group_1['size of group'] = int(r[3],16)
			# individual cell module temperatures
			line = r[4]
			n = 2
			individual_cells = [line[i:i+n] for i in range(0, len(line), n)]
			individual_cells_dict = {}
			i = 1
			for cell in individual_cells:	
				individual_cells_dict['cell '+str(i)] = int(cell, 16)
				i += 1
			cell_group_1['individual cell module temperatures'] = individual_cells_dict
			data['cell group 1'] = cell_group_1
			limit = int(r[3],16)
			for i in range(limit-1):
				response = self.ser.readline().decode('ascii')
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BT2"
				cell_group_x = {}
				cell_group_x['cell string number'] = int(r[1],16)
				cell_group_x['cell number of first cell in group'] = int(r[2],16)
				cell_group_x['size of group'] = int(r[3],16)
				# individual cell module temperatures
				line = r[4]
				n = 2
				individual_cells = [line[i:i+n] for i in range(0, len(line), n)]
				individual_cells_dict = {}
				i = 1
				for cell in individual_cells:	
					individual_cells_dict['cell '+str(i)] = int(cell, 16)
					i += 1
				cell_group_1['individual cell module temperatures'] = individual_cells_dict
				data['cell group '+str(x+2)] = cell_group_x
			return data
	def BT3(self):
		"""
		Battery Cell Temperature Summary Sentence
		This sentence contains the summary of cell temperature values of the battery pack. It is sent periodically with configurable time intervals for active and sleep states (Data Transmission to Display Period).		
		"""
		sentence = "BT3,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT3"
		
		if r[1] == '':
			return {"Cells cannot be communicated to."}
		else:
			data = {}
			numberOfCells = int(r[1],16)
			minCellTemp = int(r[2],16) - 100
			maxCellTemp = int(r[3],16) - 100
			averageCellTemp = int(r[4],16) - 100
			data['number of cells'] = numberOfCells
			data['minimum cell temperature'] = minCellTemp
			data['maximum cell temperature'] = maxCellTemp
			data['average cell temperature'] = averageCellTemp
			return data
			
			#return [numberOfCells,minCellTemp,maxCellTemp,averageCellTemp]
	def BT4(self):
		"""
		BT4 – Battery Cell Temperature Detail Sentence
		This sentence contains individual cell temperatures of a group of cells. Each group consists of 1 to 8 cells. 
		"""
		#construct the sentence
		sentence = "BT4,?,"
		number = crc8(sentence)
		sentence += number
		#send it
		self.execute(sentence)
		
		#ask for a response.
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BT4"
		
		#return an empty dictionary with this error message
		if r[1] == '':
			return {"Cells cannot be communicated to."}
		else:
			data = {}
			cell_group_1 = {}
			cell_group_1['cell string number'] = int(r[1],16)
			cell_group_1['cell number of first cell in group'] = int(r[2],16)
			cell_group_1['size of group'] = int(r[3],16)
			line = r[4]
			n = 2
			individual_cells = [line[i:i+n] for i in range(0, len(line), n)]
			individual_cells_dict = {}
			i = 1
			for cell in individual_cells:	
				individual_cells_dict['cell '+str(i)] = int(cell, 16)
				i += 1
			cell_group_1['individual cell temperatures'] = individual_cells_dict
			data['cell group 1'] = cell_group_1
			limit = int(r[3],16)
			for x in range(limit-1):
				cell_group_x = {}
				cell_group_x['cell string number'] = int(r[1],16)
				cell_group_x['cell number of first cell in group'] = int(r[2],16)
				cell_group_x['size of group'] = int(r[3],16)
				line = r[4]
				n = 2
				individual_cells = [line[i:i+n] for i in range(0, len(line), n)]
				individual_cells_dict = {}
				i = 1
				for cell in individual_cells:	
					individual_cells_dict['cell '+str(i)] = int(cell, 16)
					i += 1
				cell_group_x['individual cell temperatures'] = individual_cells_dict
				data['cell group ' + str(x+2)] = cell_group_x
			return data
	def BV1(self):
		sentence = "BV1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BV1"
		
		if r[1] == '':
			return {"Cannot communicate to cells."}
		else:
			numberOfCells = int(r[1],16)
			minCellVoltage = (int(r[2],16) + 200 ) * 0.01
			maxCellVoltage = (int(r[3],16) + 200 ) * 0.01
			averageCellVoltage = (int(r[4],16) + 200 ) * 0.01
			totalVoltage = (int(r[2],16) ) * 0.01
			data = {}
			data['number of cells'] = numberOfCells
			data['minimum cell voltage'] = minCellVoltage
			data['maximum cell voltage'] = maxCellVoltage
			data['average cell voltage'] = averageCellVoltage
			data['total voltage'] = totalVoltage 
			return data
			#return [numberOfCells,minCellVoltage,maxCellVoltage,averageCellVoltage,totalVoltage]
	def BV2(self):
		"""
		Battery Voltage Detail Sentence
		This sentence contains individual voltages of a group of cells. Each group consists of 1 to 8 cells.
		"""
		#construct the sentence, then send it.
		sentence = "BV2,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		#get the response, and check if it's valid.
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "BV2"
		
		#check for empty string. if it's empty, return an empty array.
		if r[1] == '':
			return {"Cannot communicate to cells."}
		else:
			data = {}
			cell_group_1 = {}
			cell_group_1['cell string number'] = int(r[1],16)
			cell_group_1['cell number of first cell in group'] = int(r[2],16)
			cell_group_1['size of group'] = int(r[3],16)
			line = r[4]
			n = 2
			individual_cells = [line[i:i+n] for i in range(0, len(line), n)]
			individual_cells_dict = {}
			i = 1
			for cell in individual_cells:	
				individual_cells_dict['cell '+str(i)] = int(cell, 16)
				i += 1
			cell_group_1['individual cell voltages'] = individual_cells_dict
			data['cell group 1'] = cell_group_1
			limit = int(r[3],16)
			for x in range(limit-1):
				#read the next sentence, and intepret it
				response = self.ser.readline().decode('ascii')
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == "BV2"
				
				cell_group_x = {}
				cell_group_x['cell string number'] = int(r[1],16)
				cell_group_x['cell number of first cell in group'] = int(r[2],16)
				cell_group_x['size of group'] = int(r[3],16)
				line = r[4]
				n = 2
				individual_cells = [line[i:i+n] for i in range(0, len(line), n)]
				individual_cells_dict = {}
				i = 1
				for cell in individual_cells:	
					individual_cells_dict['cell '+str(i)] = int(cell, 16)
					i += 1
				cell_group_x['individual cell voltages'] = individual_cells_dict
				data['cell group ' + str(x+2)] = cell_group_x				
			return data
			
	def CF2(self, parameterID):
		"""
		parameterID must be an integer.
		
		returns the parameter. Must be processed separately.
		"""
		sentence = "CF2," + str(parameterID.hex()) + ",?"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CF2"
		assert r[1] == str(parameterID.hex())
		
		data = {}
		data['parameter ID'] = parameterID
		data['unprocessed data'] = r[2]
		return data
	def CG1(self):
		"""
		Can Devices Status Sentence
		
		This sentence contains the statuses of Emus internal CAN peripherals.

		"""
		sentence = "CG1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CG1"
		
		CAN_current_dict = {
			0 :" Not configured",
			1 : "OK",
			2 : "Error",
			3 : "No Response."
		}
		CAN_current_sensor_status = CAN_current_dict[int(r[1],16)]
		
		data = {}
		data['CAN current sensor status'] = CAN_current_sensor_status
		X = 1
		for i in range(3,67,2):
			number_of_cells = int(r[i],16)
			status = CAN_current_dict(int(r[i+1],16))
			#create a separate dictionary for each cell.
			ii = {}
			ii['number of cells'] = number_of_cells
			ii['status'] = status
			#add that dictionary to the data pool as CAN cell group X.
			data['CAN cell group ' + str(X)] = ii 
			X += 1
		return data

	def CN1(self):	
		"""
		Received CAN Message Sentence	
		This sentence reports the CAN messages received on CAN bus by Emus BMS Control Unit, if “Send to RS232/USB” function is enabled.

		"""
		#construct the sentence, and send it.
		sentence = "CN1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		#get the response. should only be 1 line.
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CN1"
		data = {}
		CANIdentifier = int(r[1],16)
		identifierExtensionFlag = True if r[2] == '1' else False
		remoteTransmissionRequestFlag = True if r[3] == '1' else False
		dataLength = int(r[4],10)
		data['CAN Identifier'] = CANIdentifier
		data['Identifier Extension Used'] = identifierExtensionFlag
		data['Remote Transmission Used'] = remoteTransmissionRequestFlag
		data['Data Length'] = dataLength
		line = [r[5][i:i+2] for i in range(0,len(r[5]),2)]
		data['Unprocessed CAN Data'] = line
		return data
	def CN2(self):
		"""
		Sent CAN Message Sentence
		reports the CAN messages sent on CAN bus if "Send to RS232/USB function is enabled.
		"""
		#construct the sentence.
		sentence = "CN2,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		#receive the response.
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CN2"
		CANIdentifier = int(r[1],16)
		identifierExtensionFlag = True if r[2] == '1' else False
		remoteTransmissionRequestFlag = True if r[3] == '1' else False
		dataLength = int(r[4],10)
		line = [r[5][i:i+2] for i in range(0,len(r[5]),2)]
		data = {}
		data['CAN Identifier'] = CANIdentifier
		data['Identifier Extension Used'] = identifierExtensionFlag
		data['Remote Transmission Used'] = remoteTransmissionRequestFlag
		data['Data Length'] = dataLength
		data['Unprocessed CAN Data'] = line
		return data
	def CS1(self):
		"""
			contains the parameters and status of the charger.
			
		"""
		sentence = "CS1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CS1"
		
		numberOfConnectedChargers = int(r[1],16)
		CANChargerStatus = int(r[2],16) #consult the CAN charger manual for the meaning.
		setVoltage = int(r[3],16)*0.1
		setCurrent = int(r[4],16)*0.1
		actualVoltage = int(r[5],16)*0.1
		actualCurrent = int(r[6],16)*0.1
		data = {}
		data['set voltage'] = setVoltage
		data['set current'] = setCurrent
		data['actual voltage'] = actualVoltage
		data['actual current'] = actualCurrent
		data['number of connected chargers'] = numberOfConnectedChargers
		data['CAN Charger Status'] = CANChargerStatus
		return data
	def CV1(self):
		"""
			contains the values of total voltage of battery pack,
			and current flowing through the battery pack.
		"""
		sentence = "CV1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "CV1"
		totalVoltage = int(r[1],16)*0.01
		current = int(r[2],16)*0.1
		data = {}
		data['total voltage'] = totalVoltage
		data['current'] = current
		return data
	def DT1(self):
		""" This is a placeholder for an electric vehicle sentence.
		This is being programmed for a greenhouse, so this will not
		be programmed for.
		"""
		return
	def FD1(self):
		"""
			This function resets the unit to factory defaults. Use at your own risk.
		"""
		sentence = "FD1,,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		return True
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
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "IN1"
		bitField = int(r[1],16)
		AC_SENSE = True if (bitField & 0x08) else False 
		IGN_IN  = True if (bitField & 0x10) else False 
		FAST_CHG = True if (bitField & 0x20) else False
		data = {}
		data['AC SENSE'] = AC_SENSE
		data['IGN IN'] = IGN_IN
		data['FAST CHG'] = FAST_CHG
		return data
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
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
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
		data = {}
		data['log event sequence number'] = int(r[1],16)
		data['log event'] = logEventDictionary[int(r[1],16)]
		y2kTimestamp = int(r[4],16) #coded in seconds since January 1, 2000 time 00:00 (Y2K)
		#Unix epoch is January 1, 1970 00:00
		#add Y2K in epoch time 
		epochTimestamp = y2kTimestamp + self.y2kInEpoch 
		data['unix timestamp'] = epochTimestamp
		
		#convert epoch time stamp into a real class from the time library.
		#import time
		#timestamp = str(time.gmtime(epochTimestamp))
		return data
	def OT1(self):
		"""
			Returns status of output pins.
			[Charger pin, heater, bat. low, buzzer, chg. ind.]
		"""
		sentence = "OT1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "OT1"
		
		CHARGER_PIN = True if (int(r[1],16) & 0x40) else False
		bitfield = int(r[3],16)
		HEATER = True if (bitfield & 0x08) else False
		BAT_LOW = True if (bitfield & 0x10) else False
		BUZZER = True if (bitfield & 0x20) else False
		CHG_IND = True if (bitfield & 0x40) else False 
		data = {}
		data['CHARGER_PIN'] = CHARGER_PIN
		data['HEATER'] = HEATER
		data['BAT_LOW'] = BAT_LOW
		data['BUZZER'] = BUZZER
		data['CHG_IND'] = CHG_IND
		return data
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
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == "PW1"
		
		authenticationCode = int(r[1],16)
		return {'authentication code': authenticationCode }
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
		elif request == 'S': #set a new password
			setence += str(newPassword) + ","
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		
		response = self.ser.readline().decode('ascii')
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
		self.execute(sentence)
		return
	def RS1(self):
		"""
			Resets the Emus BMS control unit entirely. Like a sudo reboot on a
			linux machine.
		"""
		sentence = "RS1,,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		return
	def RS2(self):
		"""
		Reset Source History Log Sentence
		This sentence is used to retrieve the reset source history log.
		"""
		sentence = "RS2,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == 'RS2'
		data = {}
		j = 1
		for i in range(1,10,2):
			timestamp =  int(r[i],16)+ self.y2kInEpoch
			x = int(r[i+1],16)
			POWER_ON_RESET = True if x & 0x1 else False
			EXTERNAL_RESET = True if x & 0x2 else False
			BROWN_OUT_RESET = True if x & 0x4 else False
			WATCHDOG_RESET = True if x & 0x8 else False
			JTAG_RESET = True if x & 0x10 else False
			STACK_OVERFLOW_RESET = True if x & 0x20 else False
			USER_CAUSED_RESET = True if x & 0x40 else False
			ii = {}
			ii['POWER_ON_RESET'] = POWER_ON_RESET
			ii['EXTERNAL_RESET'] = EXTERNAL_RESET
			ii['BROWN_OUT_RESET'] = BROWN_OUT_RESET
			ii['WATCHDOG_RESET'] = WATCHDOG_RESET
			ii['JTAG_RESET'] = JTAG_RESET
			ii['STACK_OVERFLOW_RESET'] = STACK_OVERFLOW_RESET
			ii['USER_CAUSED_RESET'] = USER_CAUSED_RESET
			data['record ' + str(j)] = ii
			j += 1
		return data
	
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
			self.execute(sentence)
			return True
	def SS1(self, request, statisticIdentifier=0):
		"""
		This method is used to retrive the statistics from the Emus BMS unit.
		request parameter:
		
		'?': request all statistics
		'N': request a numbered statistic. Pass in a number.
		'c': clear all unprotected statistics.
		"""
		if request == '?':
			#assemble the sentence
			sentence = "SS1,?,"
			number = crc8(sentence)
			sentence += number
			self.execute(sentence)
			
			#read all lines that are sent in response. I don't know how many lines there are.
			#times out after 500 seconds.
			#The code will process all the lines, though.
			#each line contains a line.
			#validate every line.
			all_responses = self.ser.readlines(500)
			data = {}
			j = 1
			for response in all_responses:
				assert crc8(response[:2]) == int(response[-2:]) # crc check
				r = response.split(',')
				assert r[0] == 'SS1'
				datum = BMSstatistic(int(r[1],16),int(r[2],16),int(r[3],16),int(r[4],16))
				data['statistic ' + str(j)] = datum
			return data
		if request == 'N':
			#check if it's a number.
			if not isinstance(number, int):
				return -1
			#construct the sentence.
			#send the data in hex.
			sentence = "SS1," + hex(statisticIdentifier)[2:].upper() + ","
			number = crc8(sentence)
			sentence += number
			self.execute(sentence)
			
			#only 1 line of response is sent.
			response = self.ser.readline().decode('ascii')
			assert crc8(response[:2]) == int(response[-2:]) # crc check
			r = response.split(',')
			assert r[0] == 'SS1'
			#this must be true. We have to be getting the statistic we asked for.
			assert int(r[1],16) == statisticIdentifier
			
			statisticValue = int(r[2], 16)
			statisticValueAdditionalInfo = int(r[3],16)
			timeStamp = int(r[4],16)
			
			single_statistic = BMSstatistic(statisticsIdentifier, statisticValue,statisticValueAdditionalInfo,timeStamp)
			return single_statistic
			
		if request == 'c':
			#assemble the sentence.
			sentence = "SS1,c,"
			number = crc8(sentence)
			sentence += number
			#send the sentence
			self.execute(sentence)
			return {}
	def	ST1(self):
		"""
			BMS Status sentence
		"""
		#construct the sentence, and send it.
		sentence = "ST1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
	
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == 'ST1'
		#let's use a dictionary for easy reading.
		chargingStageDict = {
			0 : "Charger Disconnected",
			1 : "Pre-Heating Stage",
			2 : "Pre-Charging Stage",
			3 : "Main Charging Stage",
			4 : "Balancing Stage",
			5 : "Charging Finished",
			6 : "Charging Error"
		}
		chargingErrorDict = { 
			0 : "No error",
			1 : " No cell communication at the start of charging or communication lost during Pre-charging (using CAN charger), cannot charge",
			2 : " No cell communication (using non-CAN charger), cannot charge",
			3 : " Maximum charging stage duration expired;",
			4 : " Cell communication lost during Main Charging or Balancing stage (using CAN charger), cannot continue charging",
			5 : " Cannot set cell module balancing threshold; ",
			6 : " Cell or cell module temperature too high;",
			7 : " Cell communication lost during Pre-heating stage (using CAN charger);",
			8 : " Number of cells mismatch;",
			9 : " Cell over-voltage;",
			10 : " Cell protection event occurred."
		}
		data = {}
		#find all the errors using the dictionaries above.
		data['charging stage'] = chargingStageDict[int(r[1],16)]
		data['last charging error'] = chargingErrorDict[int(r[2],16)]
		data['last charging error parameter'] = int(r[3],16)
		data['stage duration'] = int(r[4],16) # in seconds.
		
		#bitfields.
		status_bitfield = int(r[5],16)
		
			
		data['Valid cell voltages'],data['Valid balancing rates'],data['valid number of live cells'], data['battery charging finished'],data['valid cell temperatures']=bitAt(status_bitfield,0),bitAt(status_bitfield,1),bitAt(status_bitfield,2),bitAt(status_bitfield,3),bitAt(status_bitfield,4),bitAt(status_bitfield,5)
		
		protection_bitfield = int(r[6],16)
		
		data['undervoltage'],data['overvoltage'],data['discharge overcurrent'],data['charge overcurrent'],data['cell module overheat'],data['leakage'],data['no_cell_comm,cell_overheat'] = bitAt(protection_bitfield,0),bitAt(protection_bitfield,1),bitAt(protection_bitfield,2),bitAt(protection_bitfield,3),bitAt(protection_bitfield,4),bitAt(protection_bitfield,5),bitAt(protection_bitfield,6),bitAt(protection_bitfield,11)
		
		power_bitfield = int(r[7],16)
		data['warning: power reduction: low voltage'],data['warning: power reduction: high current'],data['warning: power reduction: high cell module temperature'], data['warning: power reduction: high cell temperature'] = bitAt(power_bitfield,0),bitAt(power_bitfield,1),bitAt(power_bitfield,2),bitAt(power_bitfield,5)
		
		pin_bitfield = int(r[8],16)
		data['no_function'],data['speed_sensor'],data['fast_charge_switch'],data['ign_key'],data['charger_mains_AC_sense'],data[' heater_enable'],data['sound_buzzer'],data['battery_low'],data['charging_indication'],data['charger_enable_output'],data['state_of_charge'],data['battery_contactor'],data['battery_fan'],data['current_sensor'],data['leakage_sensor'],data['power_reduction'],data['charging_interlock'],data[' analog_charger_control'],data[' ZVU_boost_charge'],data['ZVU_slow_charge'],data['ZVU_buffer_mode'],data['BMS_failure'],data['equalization_enable'],data['DCDC_control'],data['ESM_rectifier_current_limit'],data['contactor_precharge'] = bitAt(pin_bitfield,0),bitAt(pin_bitfield,1),bitAt(pin_bitfield,2),bitAt(pin_bitfield,3),bitAt(pin_bitfield,4),bitAt(pin_bitfield,5),bitAt(pin_bitfield,6),bitAt(pin_bitfield,7),bitAt(pin_bitfield,8),bitAt(pin_bitfield,9),bitAt(pin_bitfield,10),bitAt(pin_bitfield,11),bitAt(pin_bitfield,12),bitAt(pin_bitfield,13),bitAt(pin_bitfield,14),bitAt(pin_bitfield,15),bitAt(pin_bitfield,16),bitAt(pin_bitfield,17),bitAt(pin_bitfield,18),bitAt(pin_bitfield,19),bitAt(pin_bitfield,20),bitAt(pin_bitfield,21),bitAt(pin_bitfield,22),bitAt(pin_bitfield,23),bitAt(pin_bitfield,24),bitAt(pin_bitfield,25),bitAt(pin_bitfield,26),
		return data
	def TD1(self):
		"""
		Time and date according to the BMS unit.
		"""
		sentence = "TD1,?,"
		number = crc8(sentence)
		sentence += number
		self.execute(sentence)
	
		response = self.ser.readline().decode('ascii')
		assert crc8(response[:2]) == int(response[-2:]) # crc check
		r = response.split(',')
		assert r[0] == 'TD1'
		year = int(r[1],10)
		month = int(r[2],10)
		day = int(r[3],10)
		hour = int(r[4],10)
		minute = int(r[5],10)
		second = int(r[6],10)
		uptime = int(r[7],16)
		data = {}
		data['year'] = year
		data['month'] = month
		data['day'] = day
		data['hour'] = hour
		data['minute'] = minute
		data['second'] = second
		data['uptime'] = uptime
		return data
	def TC2(self):
		"""
			Used to calibrate cell temperature by a PC, not a microcontroller. Do not use!
		"""
		return -1
	def DumpToJSONfile(self, JSON_file_pointer):	
		"""
			Dumps all data to a JSON file that you pass in.
		"""
		import json
		BatteryBalancingRateSummary = self.BB1()
		BatteryBalancingRateDetail = self.BB2()
		
		BatteryCharge = self.BC1()
		
		BatteryModuleTemperatureSummary = self.BT1()
		BatteryModuleTemperatureDetail = self.BT2()
		BatteryCellTemperatureSummary = self.BT3()
		BatteryCellTemperatureDetail = self.BT4()
		
		BatteryVoltageSummary = self.BV1()
		BatteryVoltageDetail = self.BV2()
		
		CANDevicesStatus = self.CG1()
		ReceivedCANMessages = self.CN1()
		
		ChargerStatus = self.CS1()
		CurrentAndVoltage = self.CV1()
		
		DistanceAndEnergy = self.DT1()
		
		InputPins = self.IN1()
		
		EventsLog = self.LG1()
		
		OutputPins = self.OT1()
		
		Statistics = self.SS1()
		
		BMSStatus = self.ST1()
		
		TimeAndDate = self.TD1()
		
		VersionNumber = self.VR1()
		
		data = {}
		data['BatteryBalancingRateSummary'] = BatteryBalancingRateSummary
		data['BatteryBalancingRateDetail'] = BatteryBalancingRateDetail
		data['BatteryCharge'] = BatteryCharge
		data['BatteryModuleTemperatureSummary'] = BatteryModuleTemperatureSummary
		data['BatteryModuleTemperatureDetail'] = BatteryModuleTemperatureDetail
		data['BatteryVoltageSummary'] = BatteryVoltageSummary
		data['BatteryVoltageDetail'] = BatteryVoltageDetail
		data['CANDevicesStatus'] = CANDevicesStatus 
		data['ReceivedCANMessages'] = ReceivedCANMessages
		data['ChargerStatus'] = ChargerStatus
		data['CurrentAndVoltage'] = CurrentAndVoltage
		data['DistanceAndEnergy'] = DistanceAndEnergy
		data['InputPins'] = InputPins
		data['EventsLog'] = EventsLog
		data['OutputPins'] = OutputPins
		data['Statistics'] = Statistics
		data['BMSStatus'] = BMSStatus
		data['TimeAndDate'] = TimeAndDate
		data['VersionNumber'] = VersionNumber
		json.dump(data, JSON_file_pointer)
		
#testing grounds
if __name__ == "__main__":
	try:
		greenhouseBMS = BMS("COM1", 57600)		
		test = open("test.json","rw")
		greenhouseBMS.DumpToJSONfile(test)
	except:
		pass
def bitAt(bitfield, position):
	return True if (bitfield & (0x1 << position)) else False