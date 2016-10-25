import os 
import csv


def readFrequenceStation(File_Path,File_Name):
	
	FeaquenceStation_Record = list()
	
	os.chdir(File_Path)
	inFile = open(File_Name,'r')
	for the_line in csv.reader(inFile):
		FeaquenceStation_Record.append(the_line)
	
	return FeaquenceStation_Record
'''
File_Path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Analysis_OD_Top10_9/'+'000'
File_Name 	= 'Top10Frequence_0.88.txt'
readFrequenceStation(File_Path,File_Name)
'''