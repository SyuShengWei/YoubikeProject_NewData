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

O_Station = 0
D_Station = 70
Period    = 10

infile_path = File_Path + str(O_Station).rjust(3,'0')

Top10_Record = RTR.readTop10Record(infile_path,File_number,File_OD,File_ODR,num_period,num_recordday)

Station_OD_List = RV.readValue(str(D_Station),Period,Top10_Record,'ODR')

x = np.arange(0,len(Station_OD_List))

plt.plot(x,Station_OD_List)	
plt.show()