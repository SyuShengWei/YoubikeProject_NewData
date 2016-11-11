import os 
import Function_readDataValue as RDV

def classfy (Data_List):
	Percentage_List = [ 0 for Percentage in range(10) ]
	Station_List = [ [] for Percentage in range(10) ]
	for value in Data_List :
		if   value < 0.1 :
			Percentage_List[0] += 1
			Station_List[0].append(Data_List.index(value))
		elif value < 0.2 and value >= 0.1 :
			Percentage_List[1] += 1
			Station_List[1].append(Data_List.index(value))
		elif value < 0.3 and value >= 0.2 :
			Percentage_List[2] += 1
			Station_List[2].append(Data_List.index(value))
		elif value < 0.4 and value >= 0.3 :
			Percentage_List[3] += 1
			Station_List[3].append(Data_List.index(value))
		elif value < 0.5 and value >= 0.4 :
			Percentage_List[4] += 1
			Station_List[4].append(Data_List.index(value))
		elif value < 0.6 and value >= 0.5 :
			Percentage_List[5] += 1
			Station_List[5].append(Data_List.index(value))
		elif value < 0.7 and value >= 0.6 :
			Percentage_List[6] += 1
			Station_List[6].append(Data_List.index(value))
		elif value < 0.8 and value >= 0.7 :
			Percentage_List[7] += 1
			Station_List[7].append(Data_List.index(value))
		elif value < 0.9 and value >= 0.8 :
			Percentage_List[8] += 1
			Station_List[8].append(Data_List.index(value))
		elif value < 1   and value >= 0.9 :
			Percentage_List[9] += 1
			Station_List[9].append(Data_List.index(value))
			
	return Percentage_List , Station_List



infile_path = 'C:/Users/SyuShengWei/Desktop/ODData/'

which_file_control = input("1.Peroid 2.Station 3.Station_Skip : ")

Percentage_List = []
Index_List =[]

if which_file_control == '1' :
	file_name = 'ConfidencePeriod_pass.txt'
	print(file_name)
	Data_List = []
	RDV.readData(Data_List,infile_path + file_name)
	Percentage_List , Index_List = classfy(Data_List)	
elif which_file_control == '2' :
	file_name = 'ConfidenceStation_pass.txt'
	Data_List = []
	RDV.readData(Data_List,infile_path + file_name)
	Percentage_List , Index_List = classfy(Data_List)
elif which_file_control == '3' :
	file_name = 'ConfidenceStation_Skip_pass.txt'
	Data_List = []
	RDV.readData(Data_List,infile_path + file_name)
	Percentage_List , Index_List = classfy(Data_List)
	
for i in range(9,-1,-1):
	print("{}0%up : {}".format(i,Percentage_List[i]))
	#print(Index_List[i])