import os
import Function_readTop10Record    as RTR
import Function_scanTop10Frequence as STF 
NUM_PERIOD    =  48
NUM_STATION   = 196
NUM_RECORDDAY =  28
for floder in os.listdir('C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Analysis_OD_Top10_9'):
	
	File_Path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Analysis_OD_Top10_9/'+floder
	File_Name_Num 	= 'Station_Num_10.csv'	
	File_Name_OD 	= 'Station_OD_10.csv'	
	File_Name_ODR 	= 'Station_ODR_10.csv'	
	os.chdir(File_Path)
	
	Top10_Record = RTR.readTop10Record(File_Path,File_Name_Num,File_Name_OD,File_Name_ODR,NUM_PERIOD,NUM_RECORDDAY)
    #scan the file to find station
	Frequence_Analysis = STF.scanTop10Frequence(Top10_Record,NUM_PERIOD,NUM_RECORDDAY)
	Frequence_Record   = Frequence_Analysis[0]
	Frequence_Period_Value_List = Frequence_Analysis[1]
	
	frequence_bound_rate = 0.88
	
	Frequently_List = list()
	for Period in range(0,NUM_PERIOD):
		Period_List = list()
		for stationRecord in Frequence_Record[Period]:
			frequently = round(stationRecord.getFre() / Frequence_Period_Value_List[Period],5)
			if frequently >= frequence_bound_rate:
				Period_List.append(stationRecord.getNum())
		Frequently_List.append(Period_List)
		#if Period_List != []:
			#print("period {}: station {}frequency station".format(str(Period).rjust(2,' '),Period_List))
	

	if os.path.isfile('Top10Frequence_'+str(frequence_bound_rate)+'.txt'):
		os.remove('Top10Frequence_'+str(frequence_bound_rate)+'.txt')
	
	
	outFile = open('Top10Frequence_'+str(frequence_bound_rate)+'.txt','a')
	for Period in range(0,NUM_PERIOD):
		if Frequently_List[Period] != [] :
			for station in range(0,len(Frequently_List[Period])):
				outFile.write(Frequently_List[Period][station])
				if station != len(Frequently_List[Period]) -1 :
					outFile.write(',')
		if Period != NUM_PERIOD -1 :
			outFile.write('\n')
	outFile.close()
	
	break
	




