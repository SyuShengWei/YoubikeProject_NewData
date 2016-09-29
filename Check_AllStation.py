import os 
from Function_readData import *

if not os.path.exists('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num'):
	os.makedirs('Station_Num')
	
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/103'):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/103')
	Station_List = list()
	Data_List = list()
	readData(Data_List,filename,0)
	for the_line in Data_List:
		Line_Info = the_line.split(',')
		if '@' in Line_Info[2] or Line_Info[2] == '':continue
		if Line_Info[2] not in Station_List:
			Station_List.append(Line_Info[2])
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num')			
	outFile = open('All_Stations'+filename.strip('.csv')+'.txt','a')
	for data in Station_List:
		outFile.write(data)
		outFile.write('\n')
	outFile.close()


for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/104'):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/104')
	Data_List = list()
	readData(Data_List,filename,0)
	for the_line in Data_List:
		Line_Info = the_line.split(',')
		if '@' in Line_Info[2] or Line_Info[2] == '':continue
		if Line_Info[2] not in Station_List:
			Station_List.append(Line_Info[2])
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num')			
	outFile = open('All_Stations'+filename.strip('.csv')+'.txt','a')
	for data in Station_List:
		outFile.write(data)
		outFile.write('\n')