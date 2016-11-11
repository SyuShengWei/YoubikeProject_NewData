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

num_period	  = 48
num_recordday = 28
num_station   = 196

Period_List = [0 for period in range(0,num_period)]
Station_Period_List = [0 for period in range(0,num_period)]
Station_AllStation_List = [0 for period in range(0,num_period)]

for floder in os.listdir(File_Path):
	infile_path = File_Path + floder
	
	#Top10_Record list format [Period][Day][Station]
	Top10_Record = RTR.readTop10Record(infile_path,File_number,File_OD,File_ODR,num_period,num_recordday)
	#Frequence_Station list format [Period][Station]
	Frequence_Station = RFS.readFrequenceStation(infile_path,File_Name)
	
	for Period in range(0,num_period):
		len_station_list = len(Frequence_Station[Period])
		if len_station_list == 0 : continue
		for station in Frequence_Station[Period]:
			Station_OD_List = RV.readValue(station,Period,Top10_Record,'ODR')
			if len(Station_OD_List) < 20:
				continue
			else:	
				Station_AllStation_List[Period] += 1
				k , p = stats.mstats.normaltest(Station_OD_List)
				if p < 0.05 : # Does not fit normal 
					break
				else:
					if station != Frequence_Station[Period][len_station_list -1]:
						Station_Period_List[Period] += 1
						continue
					else:
						Period_List[Period] += 1
'''
outFile = open('C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Peroid_Normal_Test.txt','a')
for Period in range(0,num_period):
	element = Period_List[Period] / num_station
	outFile.write('Period {} , fit percentage {}\n'.format(str(int(Period/2)+1).rjust(2,'0'),element))
outFile.close()
'''

outFile = open('C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Peroid_Normal_Test_station.txt','a')
for Period in range(0,num_period):
	if Station_AllStation_List[Period] != 0:
		element = Station_Period_List[Period] / Station_AllStation_List[Period]
	else :
		element = 0.0000000
	outFile.write('Period {} , fit percentage {}\n'.format(str(int(Period/2)+1).rjust(2,'0'),element))
outFile.close()

