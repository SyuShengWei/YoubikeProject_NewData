'''
This Function is used to handle the Exception Station Like:
	捷運國父紀念館(二號出口) VS 捷運國館站
Thay are the same station so this Function will help me to take it as same

String1 is the station name in raw data , String2 is the station name in station infomation file
'''
def stationCompare(string1,string2):
	list1 = list(string1)
	list2 = list(string2)
	for character in list1:
		if character not in list2:
			return False
			break
		else:
			continue
	return True

'''
#check it work
import os
from Function_readData import * 

Station_Data = list()
Data_List = list()
readData(Data_List,'C:/Users/SyuShengWei/Desktop/NewDataProject/StationData/Station_Taipei.txt')
for the_line in Data_List:
	Line_Info = the_line.split(',')
	Station_Data.append(Line_Info[2])
print(Station_Data)
Data_List.clear()
readData(Data_List,'C:/Users/SyuShengWei/Desktop/NewDataProject/StationData/Station_NewTaipei.txt')
for the_line in Data_List:
	Line_Info = the_line.split(',')
	Station_Data.append(Line_Info[1])
print(Station_Data)

os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num/')
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/Station_Num/'):
	Station_List = list()
	readData(Station_List,filename,0)
	for i in range(0,len(Station_List)):
		for j in range(0,len(Station_List)):
			if i == j :continue
			else:
				if Station_List[j] in Station_Data:
					continue
				else:
					if Station_List[j] == '' : continue
					else:
						string1 = Station_List[j]
						string2 = Station_List[i]
						if not 		stationCompare(string1,string2) :
							continue
						else:
							print('Same Station :', end = ' ')
							print(string1,end =' ')
							print(string2)
'''