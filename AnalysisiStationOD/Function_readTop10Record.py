import os

class Top10Station:
	def __init__(self,station_number,station_OD,station_ODR):
		self.station_number = station_number
		self.station_OD 	= station_OD
		self.station_ODR 	= station_ODR
	
	def getNum(self):
		return self.station_number
		
	def getOD(self):
		return self.station_OD
		
	def getODR(self):
		return self.station_ODR
		
def readTop10Record(File_Path,File_number,File_OD,File_ODR,num_period,num_recordday):
	
	Top10_Record = [[[]for Day in range(num_recordday)]for Period in range(num_period)] 
	
	os.chdir(File_Path)
	inFile_num 	= open(File_number,'r')
	inFile_OD 	= open(File_OD,'r')
	inFile_ODR 	= open(File_ODR,'r')
	Data_List_num 	= inFile_num.readlines()
	Data_List_OD 	= inFile_OD.readlines()
	Data_List_ODR 	= inFile_ODR.readlines()
	
	for Period in range(0,num_period):
	#Data fo each line means data in a Period
		the_line_num = Data_List_num[Period].strip('\n')
		the_line_OD  = Data_List_OD[Period].strip('\n')
		the_line_ODR = Data_List_ODR[Period].strip('\n')
	#Data of each day is seperated by ','
		Day_Record_List_num = the_line_num.split(',')
		Day_Record_List_OD  = the_line_OD.split(',')
		Day_Record_List_ODR = the_line_ODR.split(',')
		for Day in range(0,num_recordday):
			day_record_num = Day_Record_List_num[Day]
			day_record_OD  = Day_Record_List_OD[Day]
			day_record_ODR = Day_Record_List_ODR[Day]
			if day_record_num == ' ':
				continue
			station_record_num = day_record_num.split('-')
			station_record_OD 	= day_record_OD.split('-')
			station_record_ODR = day_record_ODR.split('-')
			for i in range(0,len(station_record_num)):
				try:
					new_record = Top10Station(station_record_num[i],int(station_record_OD[i]),float(station_record_ODR[i]))
					Top10_Record[Period][Day].append(new_record)
				except:
					print('file {} , period {} , day {}'.format(File_Path,Period,Day))
					print("station{} OD{} ODR{} ".format(station_record_num[i],station_record_OD[i],station_record_ODR[i]))
	return Top10_Record