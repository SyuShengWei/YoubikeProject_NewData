# -*- coding: utf-8 -*-
"""

"""
import os

class ReadStationOD :
	
	@classmethod
	def createNew(cls,num_station,num_peroid,floder_path,Day_List):
		obj = cls()		
		obj.NUM_STATION  = num_station
		obj.NUM_PEROID   = num_peroid
		obj.FLODER_PATH  = floder_path
		obj.DAY_LIST 	  = Day_List
		obj.LEN_DAYLIST  = len(Day_List)
		#create Matrix to store OD Record of each station
		obj.Station_OD_Matrix = list()
		for Day in range(0,obj.LEN_DAYLIST):
			Day_List = list()
			for Peroid in range(0,obj.NUM_PEROID):
				Peroid_List = list()
				for D in range(0,obj.NUM_STATION):
					d_record = 0
					Peroid_List.append(d_record)
				Day_List.append(Peroid_List)
			obj.Station_OD_Matrix.append(Day_List)
		
		os.chdir(obj.FLODER_PATH)
		for Day in obj.DAY_LIST:
			inFile = open(Day + '.txt','r')
			Data_List = inFile.readlines()			
			for Peroid in range(0,obj.NUM_PEROID):
				the_line = Data_List[Peroid].strip('\n')
				Line_Info = the_line.split(',')
				for D in range(0,obj.NUM_STATION):
					element = int(Line_Info[D])
					obj.Station_OD_Matrix[obj.DAY_LIST.index(Day)][Peroid][D] = element
		return obj
		
	@classmethod
	def passList(cls,List):	
		obj = cls()
		obj.Station_OD_Matrix = List
		return obj		

	
	def printDayRecord(self,day_list_index):
		for Peroid in range(0,self.NUM_PEROID):
			for D in range(0,self.NUM_STATION):
				print(self.Station_OD_Matrix[day_list_index][Peroid][D],end='')
				if D != self.NUM_STATION -1 :
					print(',',end='')
				else:
					if Peroid != self.NUM_PEROID -1 :
						print('\n',end ='')
							
						
	def mergeDayRecord (self,merge_day):
		len_merged_matrix = int (self.LEN_DAYLIST / merge_day)		
		#create merged Matrix 		
		Merged_OD_Record = list()
		for Day in range(0,len_merged_matrix):
			Day_List = list()
			for Peroid in range(0,self.NUM_PEROID):
				Peroid_List = list()
				for D in range(0,self.NUM_STATION):
					d_record = 0
					Peroid_List.append(d_record)
				Day_List.append(Peroid_List)
			Merged_OD_Record.append(Day_List)
		
		for Day in range(0,self.LEN_DAYLIST,merge_day):
			for index in range(0,merge_day):
				for Peroid in range(0,self.NUM_PEROID):
					for D in range(0,self.NUM_STATION):
						Merged_OD_Record[int(Day/merge_day)][Peroid][D] += self.Station_OD_Matrix[Day+index][Peroid][D]
		
		return Merged_OD_Record
		
				