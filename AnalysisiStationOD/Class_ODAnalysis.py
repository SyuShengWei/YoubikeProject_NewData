# -*- coding: utf-8 -*-
"""
"""
import os

class RankStation :			
	def __init__ (self,station_Num,station_OD):
		#station_num is designed as list for same OD station
		self.station_num = station_Num
		self.station_OD = station_OD
		self.station_ODR = 0.0
		
	def getNum (self):
		return self.station_num
	
	def getOD(self):
		return self.station_OD
		
	def getODR(self):
		return self.station_ODR 
	
	def setNum (self,num):
		self.station_num = num
		
	def setOD (self,OD):
		self.station_OD = OD	
	
	def setODR(self,ODR):
		self.station_ODR = ODR



class ODAnalysis :
	
	@classmethod
	def passStationODRecord(cls,Station_OD_Record,num_station,num_period):
		obj = cls()
		obj.Station_OD_Record = Station_OD_Record
		obj.NUM_STATION = num_station
		obj.NUM_PERIOD  = num_period
		obj.NUM_RECORDDAY = len(Station_OD_Record)	
		return obj
		
	def Top10(self):
		#create a matrix to record total traveling
		#
		Total_traveling = list()
		for Day in range(0,self.NUM_RECORDDAY):
			Day_List = list()
			for Period in range(0,self.NUM_PERIOD):
				period_total = 0 
				for D in range(0,self.NUM_STATION):
					period_total += self.Station_OD_Record[Day][Period][D]
				Day_List.append(period_total)
			Total_traveling.append(Day_List)
			
		self.Top10Compare = [[[]for Period in range(0,self.NUM_PERIOD)] for Day in range(0,self.NUM_RECORDDAY) ]
		
		for Day in range(0,self.NUM_RECORDDAY):
			for Period in range(0,self.NUM_PERIOD):
				for D in range(0,self.NUM_STATION):
					if self.Station_OD_Record[Day][Period][D] == 0 :
						continue
					if self.Top10Compare[Day][Period] == []:
						new_station =  RankStation(D,self.Station_OD_Record[Day][Period][D])
						self.Top10Compare[Day][Period].append(new_station)
					else:
						for i in range(0,len(self.Top10Compare[Day][Period])):
							if self.Station_OD_Record[Day][Period][D] >= self.Top10Compare[Day][Period][i].getOD():
								new_station =  RankStation(D,self.Station_OD_Record[Day][Period][D])
								self.Top10Compare[Day][Period].insert(i,new_station)							
								break
							#last one
							if i == len(self.Top10Compare[Day][Period]) -1 :
								if self.Station_OD_Record[Day][Period][D] < self.Top10Compare[Day][Period][i].getOD():
									new_station =  RankStation(D,self.Station_OD_Record[Day][Period][D])
									self.Top10Compare[Day][Period].append(new_station)
		
							
				for i in range(0,len(self.Top10Compare[Day][Period])):
					if Total_traveling[Day][Period] == 0:
						ODR = 0
					else:
						ODR = round(self.Top10Compare[Day][Period][i].getOD() / Total_traveling[Day][Period],5)
					self.Top10Compare[Day][Period][i].setODR(ODR)
	
	def printTop10(self,station,file_path,topNum):
		if not os.path.exists(file_path):
			os.makedirs(file_path)
		os.chdir(file_path)
		
		if not os.path.exists(str(station).rjust(3,'0')):
			os.makedirs(str(station).rjust(3,'0'))
		os.chdir(file_path + '/' + str(station).rjust(3,'0'))
		#Station_NUM
		outFile1 = open('Station_Num_'	+str(topNum)+'.csv','a')
		outFile2 = open('Station_OD_'	+str(topNum)+'.csv','a')
		outFile3 = open('Station_ODR_'	+str(topNum)+'.csv','a')

		for Period in range(0,self.NUM_PERIOD):		
			for Day in range(0,self.NUM_RECORDDAY):
			#只列前10
				record_len = len(self.Top10Compare[Day][Period])
				topLen = topNum
				if record_len < topNum :
					topLen = len(self.Top10Compare[Day][Period])
					
				if topLen == 0 :
					outFile1.write(' ,')
					outFile2.write(' ,')
					outFile3.write(' ,')
					continue
				for i in range(0,topLen):
					try:
						outFile1.write(str(self.Top10Compare[Day][Period][i].getNum()))
						outFile2.write(str(self.Top10Compare[Day][Period][i].getOD()))
						outFile3.write(str(self.Top10Compare[Day][Period][i].getODR()))
					except:
						print('i{} ,day{},period{},topLen{}'.format(i,Day,Period,topLen))
					if i != topLen-1:
						outFile1.write('-')
						outFile2.write('-')
						outFile3.write('-')
					if i == 9 :
						while_index = 9
						while record_len-1 >= while_index+1 and self.Top10Compare[Day][Period][while_index+1].getOD() == self.Top10Compare[Day][Period][while_index]:
							outFile1.write(str(self.Top10Compare[Day][Period][while_index+1].getNum()))
							outFile2.write(str(self.Top10Compare[Day][Period][while_index+1].getOD()))
							outFile3.write(str(self.Top10Compare[Day][Period][while_index+1].getODR()))
							if record_len-1 >= while_index+2 and self.Top10Compare[Day][Period][while_index+2].getOD() == self.Top10Compare[Day][Period][while_index+1]:
								outFile1.write('-')
								outFile2.write('-')
								outFile3.write('-')
								while_index += 1
							else:
								break
				if Day != self.NUM_RECORDDAY - 1:
					outFile1.write(',')
					outFile2.write(',')
					outFile3.write(',')
			if Period != self.NUM_PERIOD -1:
				outFile1.write('\n')
				outFile2.write('\n')
				outFile3.write('\n')
	


		