# -*- coding: utf-8 -*-
"""
"""
import os
import Class_RankStation as RS



class ODAnalysis :
	
	@classmethod
	def passStationODRecord(cls,Station_OD_Record,num_station,num_peroid):
		obj = cls()
		obj.Station_OD_Record = Station_OD_Record
		obj.NUM_STATION = num_station
		obj.NUM_PEROID  = num_peroid
		obj.NUM_RECORDDAY = len(Station_OD_Record)	
		return obj
		
	def Top10(self):
		#create a matrix to record total traveling
		#Used to 
		Total_traveling = list()
		for Day in range(0,self.NUM_RECORDDAY):
			Day_List = list()
			for Peroid in range(0,self.NUM_PEROID):
				peroid_total = 0 
				for D in range(0,self.NUM_STATION):
					peroid_total += self.Station_OD_Record[Day][Peroid][D]
				Day_List.append(peroid_total)
			Total_traveling.append(Day_List)
			
		self.Top10Compare = list()
		for Day in range(0,self.NUM_RECORDDAY):
			Day_List = list()	
			for Peroid in range(0,self.NUM_PEROID):
				Peroid_List = list()
				for i in range(0,10):
					#station_num is designed as list for same OD station
					new_station = RS.RankStation(-1,-1)
					Peroid_List.append(new_station)
				Day_List.append(Peroid_List)
			self.Top10Compare.append(Day_List)
			
		
		for Day in range(0,self.NUM_RECORDDAY):
			for Peroid in range(0,self.NUM_PEROID):
				for D in range(0,self.NUM_STATION):
				
					if self.Station_OD_Record[Day][Peroid][D] == 0 :
						continue
					
					for i in range(0,10):
						if self.Station_OD_Record[Day][Peroid][D] > self.Top10Compare[Day][Peroid][i].getOD():
							new_station = RS.RankStation(D,self.Station_OD_Record[Day][Peroid][D])
							self.Top10Compare[Day][Peroid].insert(i,new_station)							
							del self.Top10Compare[Day][Peroid][10]
							break
						elif self.Station_OD_Record[Day][Peroid][D] == self.Top10Compare[Day][Peroid][i].getOD():
							self.Top10Compare[Day][Peroid][i].insertStation(D)
							break
				for i in range(0,10):
					if Total_traveling[Day][Peroid] == 0:
						ODR = 0
					else:
						ODR = round(self.Top10Compare[Day][Peroid][i].getOD() / Total_traveling[Day][Peroid],5)
					self.Top10Compare[Day][Peroid][i].setODR(ODR)					
	
	def printTop10(self,station,file_path,topNum):
		if not os.path.exists(file_path):
			os.makedirs(file_path)
		os.chdir(file_path)
		
		if not os.path.exists(str(station).rjust(3,'0')):
			os.makedirs(str(station).rjust(3,'0'))
		os.chdir(file_path + '/' + str(station).rjust(3,'0'))
		
		#Station_NUM
		outFile = open('Station_Num_'+str(topNum)+'.csv','a')
		for Peroid in range(0,self.NUM_PEROID):		
			for Day in range(0,self.NUM_RECORDDAY):
				for i in range(0,topNum):
					if len(self.Top10Compare[Day][Peroid][i].getNum()) == 1:
						outFile.write(str(self.Top10Compare[Day][Peroid][i].getNum()[0]))
					else:
						for j in range(0,len(self.Top10Compare[Day][Peroid][i].getNum())):
							outFile.write(str(self.Top10Compare[Day][Peroid][i].getNum()[j]))	
							if j != len(self.Top10Compare[Day][Peroid][i].getNum()) -	1:
								outFile.write(':')
							
					if i != topNum-1:
						outFile.write('-')
					else:
						if Day != self.NUM_RECORDDAY - 1:
							outFile.write(',')
						else:
							if Peroid != self.NUM_PEROID -1:
								outFile.write('\n')
		outFile.close()
								
		outFile = open('Station_OD_'+str(topNum)+'.csv','a')
		for Peroid in range(0,self.NUM_PEROID):		
			for Day in range(0,self.NUM_RECORDDAY):
				for i in range(0,topNum):
					outFile.write(str(self.Top10Compare[Day][Peroid][i].getOD()))
					if i != topNum-1:
						outFile.write('-')
					else:
						if Day != self.NUM_RECORDDAY - 1:
							outFile.write(',')
						else:
							if Peroid != self.NUM_PEROID -1:
								outFile.write('\n')
		outFile.close()
						
		outFile = open('Station_ODR_'+str(topNum)+'.csv','a')
		for Peroid in range(0,self.NUM_PEROID):		
			for Day in range(0,self.NUM_RECORDDAY):
				for i in range(0,topNum):
					outFile.write(str(self.Top10Compare[Day][Peroid][i].getODR()))
					if i != topNum-1:
						outFile.write('-')
					else:
						if Day != self.NUM_RECORDDAY - 1:
							outFile.write(',')
						else:
							if Peroid != self.NUM_PEROID -1:
								outFile.write('\n')
		outFile.close()

		