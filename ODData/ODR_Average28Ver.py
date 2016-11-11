import os 
import numpy as np
import Function_readData as RD
import Class_ReadStationOD as RSOD

file_path = "C:/Users/SyuShengWei/Desktop/ODData/"
infile_floder = 'OD_Record_byStation'
infile_path = file_path + infile_floder

outfile_floder = 'ODR_forSimu_Average28'
outfile_path   = file_path + outfile_floder

if not os.path.exists(outfile_path):
	os.makedirs(outfile_path)

Normalday_List = []
RD.readData(Normalday_List,file_path + 'Normalday.txt')


NUM_STATION = 196
NUM_PERIOD  = 48 
NUM_MergeDay  = 9
MUM_RecordDay = int (len (Normalday_List)/ NUM_MergeDay )

Confidence = [ [ [0,0] for O in range(NUM_STATION) ] for Period in range(NUM_PERIOD)]
##Confidence[Period][station][0] = confidence data
##Confidence[Period][station][1] = confidence data


for station_index  in range(0,NUM_STATION):
	#print(station_index)
	##create string type of station_index for read file
	str_station = str(station_index).rjust(3,'0')
	station_OD_record_path = infile_path +'/'+  str_station
	
	##RSOD　data form is  [Day][Period][D]  Type:int
	##Use RSOD Class to read all normalday data
	RSOD_Normalday = RSOD.ReadStationOD.createNew(NUM_STATION,NUM_PERIOD,station_OD_record_path,Normalday_List)
	##get Merged day list 
	RSOD_Merged    = RSOD_Normalday.mergeDayRecord(NUM_MergeDay)
	del RSOD_Normalday
	
	##count ODR perday and append it in ODR_Record_List
	ODR_Record_List = [ [ [] for D in range(NUM_STATION)] for Period in range(NUM_PERIOD) ]
	
	for Period in range(NUM_PERIOD):
		for D in range(NUM_STATION):
			for Day in range(MUM_RecordDay):
				total_traveling = sum(RSOD_Merged[Day][Period])
				#print(total_traveling)
				if total_traveling != 0:
					ODR_Record_List[Period][D].append( round(RSOD_Merged[Day][Period][D]/total_traveling,5) )
				else:
					ODR_Record_List[Period][D].append( 0.0 )
	#print(ODR_Record_List)
	
	##Use np to count the ODR
	ODR_Average_List = [ [ 0.0 for D in range(NUM_STATION)] for Period in range(NUM_PERIOD) ]
	for Period in range(NUM_PERIOD):
		for D in range(NUM_STATION):
			ODR = np.average(ODR_Record_List[Period][D])
			ODR_Average_List[Period][D] = ODR
	##normalize the ODR of one OD Period 
		total_ODR_in_period = sum(ODR_Average_List[Period])
		if total_ODR_in_period != 0 :
			for D in range(NUM_STATION):
				ODR_Normalized = ODR_Average_List[Period][D] / total_ODR_in_period 
				ODR_Average_List[Period][D] = ODR_Normalized
	##
	##outFile 
	##
	'''			
	## outfile
	os.chdir(outfile_path)
	for Period in range(NUM_PERIOD):
		outfile = open(str(Period).rjust(2,'0') + '.txt' ,'a')
		for D in range(NUM_STATION):
			outfile.write( str(ODR_Average_List[Period][D]) )
			
			if D != NUM_STATION -1:
				outfile.write(' ')
			else:
				if Period != NUM_PERIOD -1 :
					outfile.write('\n')
		outfile.close()			
	'''
	##
	##Normal test 
	##
	for Period in range(NUM_PERIOD):
		for D in range(NUM_STATION):
			Test_List = ODR_Record_List[Period][D]
			test_len = len(Test_List)
			start_data_index = 0
			for index in range(test_len):
				if Test_List[index] != 0.0 :
					start_data_index = index
					break
				else:
					##only 0 in 28 days
					Confidence[Period][station_index][0] += 1
			
			
			
			