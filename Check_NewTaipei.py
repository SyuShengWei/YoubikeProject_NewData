import os 
from Function_readData import *


Taipei_Stataion_List = list()
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/StationData/')
Data_List = list ()
readData(Data_List,'Stataion_Taipei.txt',1)

for the_line in Data_List:
	Line_Info = the_line.split(',')
	Taipei_Stataion_List.append(Line_Info[2])
Data_List.clear()
	
NewTaipei_Stataion_List = list()
Data_List = list()
readData(Data_List,'Station_NewTaipei.txt',1)

for the_line in Data_List :
	Line_Info = the_line.split(',')
	NewTaipei_Stataion_List.append(Line_Info[1])
print(NewTaipei_Stataion_List)

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num'):
	print(filename)
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num')
	Station_List = list()
	readData(Station_List,filename)
	
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Scan')
	outFile = open(filename,'a')
	
	for the_station in Station_List :
		if  the_station  not in Taipei_Stataion_List :
			if the_station not in NewTaipei_Stataion_List:
				print(' not both',end = '')
				print(the_station)
				#outFile.write('\n')
				
			else :
				print(' New Tai',end = '')
				print(the_station)
				#outFile.write('\n')
	outFile.close()