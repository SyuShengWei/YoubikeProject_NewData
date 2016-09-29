import os
import codecs

Old_Station_List  = list()
New_Station_List  = list()
Comp_Station_List = list()

old_station = open('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/103/20140101~31DIGES.csv','r')
Data_List = old_station.readlines()
for the_line in Data_List :
	Line_Info = the_line.split(',')
	
	if '@' in Line_Info[2] or Line_Info[2] == '':continue
	
	if Line_Info[2] not in Old_Station_List:
		Old_Station_List.append(Line_Info[2])
old_station.close()


new_station = open('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/104/20151201~1231.csv','r')

while True :
	the_line = new_station.readline()
	if the_line == '' : break
	else:
		Line_Info = the_line.split(',')
		if '@' in Line_Info[2] or Line_Info[2] == '':continue
		if Line_Info[2] not in New_Station_List:
			New_Station_List.append(Line_Info[2])

for station in New_Station_List :
	if station not in Old_Station_List and station not in Comp_Station_List:
		Comp_Station_List.append(station)
			
			
new_station.close()

Del_Station_List = list()
for station in Old_Station_List :
	if station not in New_Station_List and station not in Del_Station_List:
		Del_Station_List.append(station)



os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')
if not os.path.exists('StationData'):
	os.makedirs('StationData')
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/StationData')

outFile = open('1415_old_station.txt','a')
for data in Old_Station_List:
	outFile.write(data)
	outFile.write('\n')
outFile.close()

outFile = open('1415_new_station.txt','a')
for data in New_Station_List:
	outFile.write(data)
	outFile.write('\n')
outFile.close()


outFile = open('1415_comp_station.txt','a')
for data in Comp_Station_List:
	outFile.write(data)
	outFile.write('\n')
outFile.close()


outFile = open('1415_del_station.txt','a')
for data in Del_Station_List:
	outFile.write(data)
	outFile.write('\n')
outFile.close()