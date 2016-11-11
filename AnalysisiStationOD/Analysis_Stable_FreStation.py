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


Level_List = [0 for i in range(0,10)]


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
			#print(the_station)
			Station_OD_List = RV.readValue(the_station,Period,Top10_Record,'ODR')
			if len(Station_OD_List) <= 8 :
				print('O station {},Peroid {},station {} less of data'.format(floder,Period,the_station))
				continue
			k,p=stats.mstats.normaltest(Station_OD_List)
			if p < 0.05:
				#print("Period {} ,the OD of station {} is Not normal".format(str(Period).rjust(2,'0'),the_station.rjust(3,'0')))
				continue
			else:
				#print("Period {} ,the OD of station {} Is FIT Normal".format(str(Period).rjust(2,'0'),the_station.rjust(3,'0')))
				fited_station +=1
	percentage = round(fited_station/total_station,5)		
	
	print(('O station {} ,Fit percentage = {}'.format(floder,percentage)))
	outFile = open('C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Normal_Test_Frequence.txt','a')
	outFile.write('O station {} ,Fit percentage = {} \n'.format(floder,percentage))
	
	if percentage >= 0 and percentage < 0.1:
		Level_List[0] += 1
	elif percentage >= 0.1 and percentage < 0.2:
		Level_List[1] += 1
	elif percentage >= 0.2 and percentage < 0.3:
		Level_List[2] += 1
	elif percentage >= 0.3 and percentage < 0.4:
		Level_List[3] += 1
	elif percentage >= 0.4 and percentage < 0.5:
		Level_List[4] += 1
	elif percentage >= 0.5 and percentage < 0.6:
		Level_List[5] += 1
	elif percentage >= 0.6 and percentage < 0.7:
		Level_List[6] += 1
	elif percentage >= 0.7 and percentage < 0.8:
		Level_List[7] += 1
	elif percentage >= 0.8 and percentage < 0.9:
		Level_List[8] += 1
	elif percentage >= 0.9 and percentage < 1.0:
		Level_List[9] += 1
outFile = open('C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Normal_Test_Frequence.txt','a')
for element in Level_List:
	outFile.write(str(element)+',')