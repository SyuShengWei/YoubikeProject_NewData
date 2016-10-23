import os
import Function_readData as Read

Normalday_List = list()
Read.readData( Normalday_List , 'C:/Users/SyuShengWei/Desktop/NewDataProject/Normalday.txt' )

NUM_STATIONS  = 213
NUM_PEROID    = 48
NUM_PEROIDLEN = 1800

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm'):
	print(filename)
	
	if filename.strip('.csv') not in Normalday_List : continue
	
	OD_Record_Matrix = list()
	for Peroid in range(0,NUM_PEROID):
		Peroid_List = list()
		for O in range(0,NUM_STATIONS):
			O_List = list()
			for D in range(0,NUM_STATIONS):
				d_record = 0
				O_List.append(d_record)
			Peroid_List.append(O_List)
		OD_Record_Matrix.append(Peroid_List)
		
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm')
	
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
		
		OD_Record_Matrix[peroid_index][o_index][d_index] += 1
	
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/')
	if not os.path.exists('OD_Record_30'):
		os.makedirs('OD_Record_30')
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OD_Record_30')
	if not os.path.exists(filename.strip('csv')):
		os.makedirs(filename.strip('csv'))
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OD_Record_30/' + filename.strip('csv') )
	
	for Peroid in range(0,NUM_PEROID):
		outFile = open(str(Peroid).rjust(2,'0')+'.txt' , 'a' )
		for O in range(0,NUM_STATIONS):
			for D in  range(0,NUM_STATIONS):
				outFile.write(str(OD_Record_Matrix [Peroid][O][D]) )
				if D != NUM_STATIONS -1 :
					outFile.write(',')
				else:
					if O != NUM_STATIONS -1:
						outFile.write('\n')
						