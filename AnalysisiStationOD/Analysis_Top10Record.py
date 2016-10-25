import Function_readData as RD
import Class_ReadStationOD as RSOD
import Class_ODAnalysis as ODA


Normalday_List = list()
RD.readData(Normalday_List,'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Normalday.txt')

newdata_project_path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/'
infile_floder = 'OD_Record_byStation'
outfile_floder = 'Analysis_OD_Top10'

infile_path = newdata_project_path + infile_floder
outfile_path = newdata_project_path +outfile_floder

NUM_STATION = 196
NUM_PERIOD = 48

for station in range(0,NUM_STATION):
	str_station = str(station).rjust(3,'0')
	RSOD2 = RSOD.ReadStationOD.createNew(NUM_STATION,NUM_PERIOD,infile_path +'/'+  str_station,Normalday_List)
	
	mergeDay = 9	
	Merged_List = RSOD2.mergeDayRecord(mergeDay)
	
	testODA = ODA.ODAnalysis.passStationODRecord(Merged_List,NUM_STATION,NUM_PERIOD)
	testODA.Top10()
	testODA.printTop10(station,outfile_path + '_' + str(mergeDay),10)
	#testODA.printTop10(station,outfile_path + '_' + str(mergeDay),5)
	break