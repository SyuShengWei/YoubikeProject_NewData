import os
import codecs

os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')

Stataion_Info_Dict = {}


inFile = open('C:/Users/SyuShengWei/Desktop/NewDataProject/StationData/Stataion_Info.txt','r' )
title_line = inFile.readline()
Data_List = inFile.readlines()

for the_line in Data_List :
	Line_Info = the_line.strip('\n')
	Line_Info = Line_Info.split(',')
	#print(Line_Info)
	if Line_Info[3] != '':
		station_name = Line_Info[3].replace('"','')
		station_info = Line_Info[8].replace('"','') +','+ Line_Info[9].replace('"','') +','+ Line_Info[4].replace('"','')
		new_dic = {station_name : station_info}
		Stataion_Info_Dict.update(new_dic)
	
'''
for key in Stataion_Info_Dict :
	print(key,end =':')
	print(Stataion_Info_Dict[key])
'''
#	


Station_Order_List  = list()

old_station = open('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/103/20140101~31DIGES.csv','r')
Data_List = old_station.readlines()
for the_line in Data_List :
	Line_Info = the_line.split(',')
	
	if '@' in Line_Info[2] or Line_Info[2] == '':continue
	
	if Line_Info[2] not in Station_Order_List:
		Station_Order_List.append(Line_Info[2])
old_station.close()

new_station = open('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/104/20151201~1231.csv','r')
Data_List = new_station.readlines()
for the_line in Data_List :
	Line_Info = the_line.split(',')
	if '@' in Line_Info[2] or Line_Info[2] == '':continue	
	if Line_Info[2] not in Station_Order_List:
		Station_Order_List.append(Line_Info[2])

new_station.close()

outFile = open('C:/Users/SyuShengWei/Desktop/NewDataProject/StationData/Station_Num_222.txt','a')
outFile.write('Station_Num,Station_Name,Station_Lat,Station,Long,Station_Capacity')
station_num_ctr = 0

for station in Station_Order_List :
	try:
		out_line = ''
		out_line += str(station_num_ctr)
		out_line += ','
		out_line += station
		out_line += ','
		out_line += Stataion_Info_Dict[station]
		out_line += '\n'
		outFile.write(out_line)
	except:
		out_line = ''
		out_line += str(station_num_ctr)
		out_line += ','
		out_line += station
		out_line += '\n'
		outFile.write(out_line)
		print(station)
	station_num_ctr += 1
outFile.close()
