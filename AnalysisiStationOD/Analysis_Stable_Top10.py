import os
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import Function_readTop10Record      as RTR
import Function_readFrequenceStation as RFS
import Function_readValue			 as RV

File_Path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Analysis_OD_Top10_9/'

File_number = 'Station_Num_10.csv'	
File_OD 	= 'Station_OD_10.csv'	
File_ODR 	= 'Station_ODR_10.csv'

File_Name 	= 'Top10Frequence_0.88.txt'

num_period = 48
num_recordday = 28

for floder in os.listdir(File_Path):
	infile_path = File_Path + floder
	
	Top10_Record = RTR.readTop10Record(infile_path,File_number,File_OD,File_ODR,num_period,num_recordday)
	Frequence_Station = RFS.readFrequenceStation(infile_path,File_Name)
	
	total_station = 0
	fited_station = 0
	
	for Period in range(0,num_period):
		for station in range(0,len(Frequence_Station[Period])):
			total_station +=1
			the_station = Frequence_Station[Period][station]
			Station_OD_List = RV.readValue(the_station,Period,Top10_Record,'ODR')
			k,p=stats.mstats.normaltest(Station_OD_List)
			if p < 0.05:
				print("Period {} ,the OD of station {} is Not normal".format(str(Period).rjust(2,'0'),the_station.rjust(3,'0')))
			else:
				print("Period {} ,the OD of station {} Is FIT Normal".format(str(Period).rjust(2,'0'),the_station.rjust(3,'0')))
				fited_station +=1
	
	print('Fit percentage = {}'.format(round(fited_station/total_station,5)))
	break