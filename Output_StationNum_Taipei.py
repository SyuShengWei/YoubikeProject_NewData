import os 
from Function_readData import *
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/StationData')

Data_List = list()
readData(Data_List,'Station_Taipei.txt',1)
outFile = open('Station_Info_Taipei.txt','a')
outFile.write('Station_Num,Station_Name,Station_Lat,Station,Long,Station_Capacity \n')
Station_Ctr = 0
for the_line in Data_List:
	Line_Info = the_line.split(',')
	station_num = Station_Ctr
	station_name = Line_Info[2]
	station_lat = Line_Info[7]
	station_long = Line_Info[8]
	station_capacity = Line_Info[3]
	outFile.write(str(station_num).rjust(3,'0') + ',' + station_name + ',' + 
					station_lat + ',' + station_long + ',' + station_capacity + '\n')
	Station_Ctr += 1
outFile.close()