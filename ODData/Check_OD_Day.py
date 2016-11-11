import os 
import csv
import Function_readData as RD

file_path = 'C:/Users/SyuShengWei/Desktop/ODData/'

Normalday_List = []
RD.readData(Normalday_List,file_path + 'Normalday.txt')
Normalday_List = Normalday_List[2:]

ODDay_Record = [ [ 0 for day in range(len(Normalday_List))] for Station in range(196)]

for dayname in Normalday_List :
	
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm')
	infile_name = dayname + '.csv'
	day_index = Normalday_List.index(dayname)
	
	infile = open(infile_name,'r')
	title_line = infile.readline()
	
	Day_Data_List = [ 0 for station in range(212)]
	
	for Line_Info in csv.reader(infile):
		if 'N-' not in Line_Info[4]:
			index = int(Line_Info[4])
			Day_Data_List[index] += 1
	infile.close()		
	for index in range(196):
		if Day_Data_List[index] != 0 :
			ODDay_Record[index][day_index] += 1
			
os.chdir('C:/Users/SyuShengWei/Desktop/ODData')
outfile = open('OD_Day.txt','a')
for station in range(196):
	for day in range(len(Normalday_List)):
		if ODDay_Record[station][day] == 0 : continue
		else :
			outfile.write(str(day)+'\n')
			break
outfile.close()