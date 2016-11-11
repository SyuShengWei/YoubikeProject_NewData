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


NotNormal = []

pic_path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Pic_Normal_OD/'
if not os.path.exists(pic_path):
	os.makedirs(pic_path)

for floder in os.listdir(File_Path):
	infile_path = File_Path + floder
	
	Top10_Record = RTR.readTop10Record(infile_path,File_number,File_OD,File_ODR,num_period,num_recordday)
	Frequence_Station = RFS.readFrequenceStation(infile_path,File_Name)
	for Period in range(0,num_period):
		if Period <= 11 : continue
		for station in range(0,len(Frequence_Station[Period])):
			the_station = Frequence_Station[Period][station]
			#print(the_station)
			Station_OD_List = RV.readValue(the_station,Period,Top10_Record,'OD')
			Station_ODR_List = RV.readValue(the_station,Period,Top10_Record,'ODR')
			if len(Station_OD_List) <= 8 :
				#outFile.write("The OD = {}:{} in Peroid = {} less of data \n".format(floder,the_station.rjust(3,'0'),str(Period).rjust(2,'0')))
				continue
			k,p=stats.mstats.normaltest(Station_OD_List)
			if p > 0.05:
			###Start to Draw
				if not os.path.exists(pic_path+str(Period).rjust(2,'0')):
					os.makedirs(pic_path+str(Period).rjust(2,'0'))
				os.chdir(pic_path+str(Period).rjust(2,'0'))

				fig = plt.figure()
				pic1 = fig.add_subplot(211)
				pic2 = fig.add_subplot(212)
				x_axis = np.arange(0,len(Station_OD_List))
				y1_axis = sorted(Station_OD_List)
				y2_axis = sorted(Station_ODR_List)
				pic1.plot(x_axis,y1_axis,'ro')
				pic1.plot(x_axis,y1_axis)
				
				pic2.plot(x_axis,y2_axis,'go')
				pic2.plot(x_axis,y2_axis)
				
				fig_title = "Period {} OD is {}_{}".format(Period,floder,the_station.rjust(3,'0'))
	
				pic1.set_title(fig_title + ' OD')
				pic1.set_ylabel('Data Value')

				pic1.grid(True)	
				
				pic2.set_title(fig_title + ' ODR')
				pic2.set_xlabel('Data Series')
				pic2.set_ylabel('Data Value')

				pic2.grid(True)	
	
				fig.savefig(str(fig_title)+'.png')
				fig.clear()
				plt.close()
			
				#outFile.write("The OD = {}:{} in Peroid = {} is not Normal".format(floder,the_station.rjust(3,'0'),str(Period).rjust(2,'0')))
				#outFile.write(" len of data = {} , {} \n".format(len(Station_OD_List),Station_OD_List))
				continue

	break