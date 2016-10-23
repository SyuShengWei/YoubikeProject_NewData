# -*- coding: utf-8 -*-

import os
import Function_readData as Read

Normalday_List = list()
Read.readData( Normalday_List , 'C:/Users/SyuShengWei/Desktop/NewDataProject/Normalday.txt' )

NUM_STATIONS  = 213
NUM_PEROID    = 48
NUM_PEROIDLEN = 1800

print('prepare')
OD_Record_Matrix = list()
for Day in range(0,len(Normalday_List)):
	Day_List = list()	
	for Peroid in range(NUM_PEROID):
		Peroid_List = list()
		for O in range(0,NUM_STATIONS):
			O_List = list()
			for D in range(0,NUM_STATIONS):
				d_record = 0
				O_List.append(d_record)
			Peroid_List.append(O_List)
		Day_List.append(Peroid_List)
	OD_Record_Matrix.append(Day_List)
print('Reading')			
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm'):
	print(filename)
	the_day = filename.strip('.csv') 
	if the_day  not in Normalday_List : continue
	
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm')
	
	day_index = Normalday_List.index(the_day)
	
	inFile = open(filename,'r')
	title_line = inFile.readline()
	Data_List = inFile.readlines()
	for the_line in Data_List:
		Line_Info = the_line.split(',')
		if 'N-' in Line_Info[4]:
			o_index = NUM_STATIONS - 1
		else: 
			o_index = int(Line_Info[4])
			
		if 'N-' in Line_Info[5]:
			d_index = NUM_STATIONS - 1
		else: 
			d_index = int(Line_Info[5])
		
		peroid_index = int(Line_Info[1]) // NUM_PEROIDLEN
		
		OD_Record_Matrix[day_index][peroid_index][o_index][d_index] += 1
print('OutFiling')		
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/')
if not os.path.exists('OD_Record_byStation'):
	os.makedirs('OD_Record_byStation')

for O in range(0,NUM_STATIONS):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OD_Record_byStation')
	if not os.path.exists(str(O).rjust(3,'0')):
		os.makedirs(str(O).rjust(3,'0'))
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OD_Record_byStation/'+ str(O).rjust(3,'0'))
	for Day in range(0,len(Normalday_List)):
		outFile = open(Normalday_List[Day]+'.txt','a')
		for Peroid in range(0,NUM_PEROID):
			for D in range(0,NUM_STATIONS):
				outFile.write(str(OD_Record_Matrix[Day][Peroid][O][D]))
				if D != NUM_STATIONS -1:
					outFile.write(',')
				else:
					if Peroid != NUM_PEROID-1:
						outFile.write('\n')
