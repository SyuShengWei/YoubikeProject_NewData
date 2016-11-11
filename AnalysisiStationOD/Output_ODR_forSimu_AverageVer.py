import os 
import numpy as np
import Function_readData as RD
import Class_ReadStationOD as RSOD


Normalday_List = list()
RD.readData(Normalday_List,'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Normalday.txt')

newdata_project_path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/'
infile_floder  = 'OD_Record_byStation'
outfile_floder = 'ODR_forSimu_AverageVer'

infile_path = newdata_project_path + infile_floder
outfile_path = newdata_project_path +outfile_floder

if not os.path.exists(outfile_path):
	os.makedirs(outfile_path)

NUM_STATION = 196
NUM_PERIOD = 48
NUM_DAYLEN = len(Normalday_List)
NUM_mergeDay = 9
NUM_recordDay = int(NUM_DAYLEN / NUM_mergeDay)

OD_Record_Matrix = [[[] for O in range(NUM_STATION)]for Period in range(NUM_PERIOD)]


for station in range(0,NUM_STATION):
	##get the row data from RSOD [Day][Period][D] ; Type:int
	str_station = str(station).rjust(3,'0')
	RSOD_Normalday = RSOD.ReadStationOD.createNew(NUM_STATION,NUM_PERIOD,infile_path +'/'+  str_station,Normalday_List)
		
	Merged_List = RSOD_Normalday.mergeDayRecord(NUM_mergeDay)
	
	Station_Record_Matrix = [[[] for D in range(NUM_STATION)]for Period in range(NUM_PERIOD)]
	
	for Period in range(NUM_PERIOD):
		for D in range(NUM_STATION):
##for every OD in a period 1.record non 0 value 2. average it and assign it to OD_Record_Matrix
			## step 1
			for Day in range(NUM_recordDay):
				if Merged_List[Day][Period][D] != 0:
					Station_Record_Matrix[Period][D].append(Merged_List[Day][Period][D])
			## step 2 
			if Station_Record_Matrix[Period][D] == [] :
				OD_Record_Matrix[Period][station].append(0.0)
			else :
				average_num = np.average(Station_Record_Matrix[Period][D])
				OD_Record_Matrix[Period][station].append(average_num)
			
if not os.path.exists(outfile_path):
	os.makedirs(outfile_path)
os.chdir(outfile_path)

for Period in range(NUM_PERIOD):
	outFile = open (str(Period).rjust(2,'0'),'a')
	for O in range(NUM_STATION):
		total_percentage = sum(OD_Record_Matrix[Period][O])
		for D in range(NUM_STATION):
			ODR = round(OD_Record_Matrix / total_percentage,5)
			outFile.write(str(ODR))
			if D != NUM_STATION-1:
				outFile.write(',')
			else:
				if O != NUM_STATION-1:
					outFile('\n')