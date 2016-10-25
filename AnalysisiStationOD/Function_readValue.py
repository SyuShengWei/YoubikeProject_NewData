#import numpy as np
#from scipy import stats
#import matplotlib.pyplot as plt

import Function_readTop10Record as RTR
import Function_readFrequenceStation as RFS


def readValue (station_num,period,Top10Record,type = 'OD'):
	
	num_recordday = len(Top10Record[0])
	
	Value_List = list()
	
	for Day in range(0,num_recordday):
		for station_index in range(0,len(Top10Record[period][Day])):
			record_station = Top10Record[period][Day][station_index]
			if station_num == record_station.getNum():
				if type == 'OD':
					Value_List.append(record_station.getOD())
				elif type == 'ODR' :
					Value_List.append(record_station.getODR())
	return Value_List

'''
NUM_RECORDDAY   = 28
NUM_PERIOD		= 48

File_Path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Analysis_OD_Top10_9/'+'000'
File_Name_Num 	= 'Station_Num_10.csv'	
File_Name_OD 	= 'Station_OD_10.csv'	
File_Name_ODR 	= 'Station_ODR_10.csv'
Top10Record = RTR.readTop10Record(File_Path,File_Name_Num,File_Name_OD,File_Name_ODR,NUM_PERIOD,NUM_RECORDDAY)

Test_List1 = readValue ('4',12,Top10Record,'OD')
Test_List2 = readValue ('4',12,Top10Record,'ODR')
for i in range(0,len(Test_List1)):
	print("OD {}, ODR {} ".format(str(Test_List1[i]).rjust(3,' '),str(Test_List2[i]).rjust(6,' ')))
	

k,p=stats.mstats.normaltest(Test_List1)

if p <0.05:
	print('Not normal')
else:
	print('Is normal')
'''