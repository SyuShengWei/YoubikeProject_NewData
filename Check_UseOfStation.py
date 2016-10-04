import os 
from Function_readData import *

os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/StationData')
Station_List = list()
readData(Station_List,'Station_Info_Taipei.txt')

Station_Record = list()
for i in range(0,len(Station_List)):
	Station_Record.append(0)

os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean')
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean'):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean')
	inFile = open(filename,'r')
	Data_List = inFile.readlines()
	for the_line in Data_List:
		Line_Info = the_line.split(',')
		o_stataion = Line_Info[2]
		d_stataion = Line_Info[4]
		for i in range(0,len(Station_List)):
			if o_stataion == Station_List[i]:
				Station_Record[i] += 1
			elif d_stataion == Station_List[i]:
				Station_Record[i] += 1 

outFile = open('C:/Users/SyuShengWei/Desktop/NewDataProject/Used_Station_Taipei.txt','a')
for data in Station_Record:
	outFile.write(str(data) + '\n')
outFile.close()