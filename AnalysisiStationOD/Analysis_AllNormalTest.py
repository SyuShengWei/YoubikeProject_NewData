import os 
import Function_readData as RD
import Class_ReadStationOD as RSOD
from scipy import stats


Normalday_List = list()
RD.readData(Normalday_List,'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Normalday.txt')

newdata_project_path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/'
infile_floder  = 'OD_Record_byStation'
outfile_floder = 'AllNormalTest_Merged'

infile_path = newdata_project_path + infile_floder
outfile_path = newdata_project_path +outfile_floder

if not os.path.exists(outfile_path):
	os.makedirs(outfile_path)

NUM_STATION = 196
NUM_PERIOD = 48
NUM_DAYLEN = len(Normalday_List)


for station in range(166,NUM_STATION):
	##get the row data from RSOD [Day][Period][D] ; Type:int
	str_station = str(station).rjust(3,'0')
	RSOD_Normalday = RSOD.ReadStationOD.createNew(NUM_STATION,NUM_PERIOD,infile_path +'/'+  str_station,Normalday_List)
	
	mergeDay = 9	
	Merged_List = RSOD_Normalday.mergeDayRecord(mergeDay)
	
	##get the Non Zero Data for Normalday Test
	OD_Record_NonZero = [[[] for D in range(NUM_STATION)] for Period in range(NUM_PERIOD)]
	for Period in range(NUM_PERIOD):
		for D in range(NUM_STATION):
			for Day in range( int (NUM_DAYLEN / mergeDay )):
				if Merged_List[Day][Period][D] != 0:
					OD_Record_NonZero[Period][D].append(Merged_List[Day][Period][D])
	##Start normal test for every OD in every Period 
	Result_Matrix = [ []  for Period in range(NUM_PERIOD)]
	
	##open lack_data_file to record less data OD 
	os.chdir(outfile_path)
	lack_data_file = open('Lack_Data.txt','a')
	not_normal_file = open('Not_Normal.txt','a')
	
	for Period in range(NUM_PERIOD):
	##result ctr 
		total_OD_in_period  = 0
		total_withdata_OD	= 0
		noraml_OD_in_period = 0
		lack_data_in_period = 0
		for D in range(NUM_STATION):
			if OD_Record_NonZero[Period][D] == []:
				continue
			elif len(OD_Record_NonZero[Period][D]) < 8 : 
				total_OD_in_period  += 1 
				lack_data_in_period += 1
				lack_data_file.write("Period : {} ,OD {}:{} lack of data \n".format( str(Period).rjust(2,'0'),str_station,str(D).rjust(3,'0')))
			else:
				total_withdata_OD +=1
				total_OD_in_period += 1 
				k,p=stats.mstats.normaltest(OD_Record_NonZero[Period][D])
				if p < 0.05: ## do not fit Noraml distribution
					not_normal_file.write("Period : {} ,OD {}:{} lack of data \n".format( str(Period).rjust(2,'0'),str_station,str(D).rjust(3,'0')))
				else:
					noraml_OD_in_period += 1
					
		if total_withdata_OD != 0 :
			normal_withdata = round( noraml_OD_in_period / total_withdata_OD  ,5)
		else :
			normal_withdata = 0.0
		
		if total_OD_in_period != 0:
			normal_total = round( noraml_OD_in_period / total_OD_in_period ,5)
			lackdata = round( lack_data_in_period / total_OD_in_period ,5)
		else: 
			normal_total = 0.0
			lackdata	 = 0.0
		Result_Matrix[Period] = [normal_withdata,normal_total,lackdata,total_OD_in_period]
	
	lack_data_file.close()
	not_normal_file.close()
	##record the percentage 
	outfile = open(str_station + '.txt','a')
	for Period in range(NUM_PERIOD):
		outfile.write("Period : {} , {}   {}fit normal , {} lack of data , total_OD = {} \n".format(  
		str(Period).rjust(2,'0') , str(Result_Matrix[Period][0]).ljust(6,'0') ,  str(Result_Matrix[Period][1]).ljust(6,'0') ,
		str(Result_Matrix[Period][2]).ljust(6,'0') , str(Result_Matrix[Period][3])))
	outfile.close()
	