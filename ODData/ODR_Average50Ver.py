import os 
import numpy as np
from scipy import stats
import Function_readData as RD
import Class_ReadStationOD as RSOD

file_path = "C:/Users/SyuShengWei/Desktop/ODData/"
infile_floder = 'OD_Record_byStation'
infile_path = file_path + infile_floder

outfile_floder = 'ODR_forSimu_Average50'
outfile_path   = file_path + outfile_floder

if not os.path.exists(outfile_path):
	os.makedirs(outfile_path)

Normalday_List = []
RD.readData(Normalday_List,file_path + 'Normalday.txt')
Normalday_List = Normalday_List[2:]

ODDay_List = []
RD.readData(ODDay_List,file_path + 'OD_Day.txt')

NUM_STATION = 196
NUM_PERIOD  = 48 
NUM_MergeDay  = 5
NUM_RecordDay = int (len (Normalday_List)/ NUM_MergeDay )
NUM_SkipPeriod = 10 

Confidence_Station = [ [0,0] for station in range(NUM_STATION) ]
Confidence_Period  = [ [0,0] for period in range(NUM_PERIOD) ]
Confidence_Station_Skip = [ [0,0] for station in range(NUM_STATION) ]


for station_index  in range(0,NUM_STATION):
	print(station_index)
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
			for Day in range(NUM_RecordDay):
				total_traveling = sum(RSOD_Merged[Day][Period])
				#print(total_traveling)
				if total_traveling != 0:
					ODR_Record_List[Period][D].append( round(RSOD_Merged[Day][Period][D]/total_traveling,5) )
				else:
					ODR_Record_List[Period][D].append( 0.0 )
	#print(ODR_Record_List[0][0])
	
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
	#deal_ctr = 0
	for Period in range(NUM_PERIOD):
		for D in range(NUM_STATION):
			Data_List = ODR_Record_List[Period][D]
			
			if sum(Data_List) == 0.0:
				Confidence_Period[Period][0] +=1						
				Confidence_Station[station_index][0] += 1
				if Period >= NUM_SkipPeriod :
					Confidence_Station_Skip[station_index][0] += 1
				#deal_ctr +=1
			else:
				day_start_index = int ( int( ODDay_List[station_index] ) / NUM_MergeDay)
				Data_List = Data_List[day_start_index:]
				k,p=stats.mstats.normaltest(Data_List)
				if p < 0.05 : ## do not fit Noraml distribution
					Confidence_Period[Period][1] +=1						
					Confidence_Station[station_index][1] += 1
					#deal_ctr += 1
					if Period >= NUM_SkipPeriod :
						Confidence_Station_Skip[station_index][1] += 1
				else:
					Confidence_Period[Period][0] +=1						
					Confidence_Station[station_index][0] += 1
					#deal_ctr +=1
					if Period >= NUM_SkipPeriod :
						Confidence_Station_Skip[station_index][0] += 1
	#print(deal_ctr)
	#break

total_OD_station = NUM_PERIOD*NUM_STATION
total_OD_station_skip = (NUM_PERIOD-NUM_SkipPeriod)*NUM_STATION
total_OD_period  = NUM_STATION*NUM_STATION
	
os.chdir(file_path)
##Normal_Test_Outfile 
outfile = open('ConfidenceStation_pass.txt','a')
for O in range(NUM_STATION):
	outfile.write( str( round( Confidence_Station[O][0] / total_OD_station , 5 ) ) )
	if O != NUM_STATION -1 :
		outfile.write('\n')
outfile.close()

outfile = open('ConfidenceStation_notpass.txt','a')
for O in range(NUM_STATION):
	outfile.write( str( round( Confidence_Station[O][1] / total_OD_station , 5 ) ) )
	if O != NUM_STATION -1 :
		outfile.write('\n')
outfile.close()

outfile = open('ConfidenceStation_Skip_pass.txt','a')
for O in range(NUM_STATION):
	outfile.write( str( round( Confidence_Station_Skip[O][0] / total_OD_station_skip , 5 ) ) )
	if O != NUM_STATION -1 :
		outfile.write('\n')
outfile.close()

outfile = open('ConfidenceStation_Skip_notpass.txt','a')
for O in range(NUM_STATION):
	outfile.write( str( round( Confidence_Station_Skip[O][1] / total_OD_station_skip , 5 ) ) )
	if O != NUM_STATION -1 :
		outfile.write('\n')
outfile.close()

outfile = open('ConfidencePeriod_pass.txt','a')
for Period in range(NUM_PERIOD):
	outfile.write( str( round( Confidence_Period[Period][0] / total_OD_period , 5 ) ) )
	if Period != NUM_PERIOD -1 :
		outfile.write('\n')
outfile.close()

outfile = open('ConfidencePeriod_notpass.txt','a')
for Period in range(NUM_PERIOD):
	outfile.write( str( round( Confidence_Period[Period][1] / total_OD_period , 5 ) ) )
	if Period != NUM_PERIOD -1 :
		outfile.write('\n')
outfile.close()
