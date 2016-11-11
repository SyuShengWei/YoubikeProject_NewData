


class StationFrequence :
	
	def __init__ (self,Station_NUM,frequence = 1):
		self.station_num = Station_NUM
		self.station_frequence = frequence
		
	def frequencePlus(self):
		self.station_frequence += 1 
	
	def getNum(self):
		return self.station_num
		
	def getFre(self):
		return self.station_frequence
	
def scanTop10Frequence(Top10_Record,num_period,num_recordday):
	#create a list to store the result data
	Frequence_Record = [[]for Period in range(0,num_period)]
	#for each Period 
	#scan all the station record in each day
	#if the station not in record -> create object of StationFrequence and add it in record
	#if the station in record -> add the frequence
	#remember to mark the station which have find
	Period_Zero_Record  = [0 for i in range(0,num_period)]
	Period_Value_Record = [0 for i in range(0,num_period)]
	
	for Period in range(0,num_period):
		for Day in range(0,num_recordday):
			if Top10_Record[Period][Day] == []:
				Period_Zero_Record[Period] += 1
			else: 
				Period_Value_Record[Period] += 1
			#start to check if station in Frequence_Record that day 			
			for station_record in Top10_Record[Period][Day]:
				if Frequence_Record[Period] == []:
					new_record = StationFrequence(station_record.getNum(),1)
					Frequence_Record[Period].append(new_record)
				else:
					if_find = 0
					for i in range(0,len(Frequence_Record[Period])):
						if station_record.getNum() == Frequence_Record[Period][i].getNum():
							Frequence_Record[Period][i].frequencePlus()
							if_find = 1
						else: continue
					if if_find == 0 :
						new_record = StationFrequence(station_record.getNum(),1)
						Frequence_Record[Period].append(new_record)
	
	result = [Frequence_Record,Period_Value_Record,Period_Zero_Record]
	return result