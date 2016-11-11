import os 
import Function_readTop10Record as RTR
import Function_readValue		as RV

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

NUM_PERIOD    =  48
NUM_STATION   = 196
NUM_RECORDDAY =  28

File_Path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Analysis_OD_Top10_9/'+'000'
File_Name_Num 	= 'Station_Num_10.csv'	
File_Name_OD 	= 'Station_OD_10.csv'	
File_Name_ODR 	= 'Station_ODR_10.csv'	
os.chdir(File_Path)
Top10_Record = RTR.readTop10Record(File_Path,File_Name_Num,File_Name_OD,File_Name_ODR,NUM_PERIOD,NUM_RECORDDAY)
#print(Top10_Record)
h = RV.readValue('4',14,Top10_Record,'ODR')
h.sort()

h_test = h[5:]


k,p = stats.mstats.normaltest(h)
print(p)
k,p = stats.mstats.normaltest(h_test)
print(p)

hmean = np.mean(h)
hstd = np.std(h)
pdf = stats.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf,'ro') # including h here is crucial

h_mean = np.mean(h_test)
h_std = np.std(h_test)
pdf_ = stats.norm.pdf(h_test, h_mean, h_std)
plt.plot(h_test, pdf_,'bo') # including h here is crucial


normpdf = np.random.normal(hmean,hstd,len(h))
normpdf.sort()
pdf = stats.norm.pdf(normpdf, hmean, hstd)
plt.plot(normpdf,pdf)
plt.show()
