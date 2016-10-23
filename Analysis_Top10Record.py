import Function_readData as RD
import Function_readStationOD as RSOD
import Function_ODAnalysis as ODA


Normalday_List = list()
RD.readData(Normalday_List,'C:/Users/SyuShengWei/Desktop/NewDataProject/Normalday.txt')

newdata_project_path = 'C:/Users/SyuShengWei/Desktop/NewDataProject/'
infile_floder = 'OD_Record_byStation'
outfile_floder = 'Analysis_OD_withoutN'

infile_path = newdata_project_path + infile_floder
outfile_path = newdata_project_path +outfile_floder


for station in range(0,212):
	str_station = str(station).rjust(3,'0')
	RSOD2 = RSOD.ReadStationOD.createNew(212,48,infile_path +'/'+  str_station,Normalday_List)
	mergeDay = 9	
	Merged_List = RSOD2.mergeDayRecord(mergeDay)
	
	testODA = ODA.ODAnalysis.passStationODRecord(Merged_List,212,48)
	testODA.Top10()
	#testODA.printTop10(station,outfile_path + '_' + str(mergeDay),10)
	#testODA.printTop10(station,outfile_path + '_' + str(mergeDay),5)
