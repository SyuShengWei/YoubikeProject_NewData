import os
import codecs
import copy

Except_List = list()
for i in range(0,12):
	Data_List = list()
	Except_List.append(Data_List)
	
Check_List = list()

FileName_List = ['20140101~31DIGES.csv','20140201~28DIGES.csv','20140301~31DIGES.csv','20140401~30DIGES.csv','20140501~31DIGES.csv','20140601~30DIGES.csv','20140701~0731DIGES.csv','20140801~0831DIGES.csv','20140901~0930DIGES.csv','20141001~1031DIGES.csv','20141103~1130DIGES.csv','20141201~1231DIGES.csv']

whitch_file = 1
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/103'):
	
	print('File : '+str(whitch_file))
	Delete_List = list()
	
	Temp_List = list()
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/103')
	inFile = codecs.open(filename, 'r')
	Data_List = inFile.readlines()
	for the_line in Data_List :
		if '@' in the_line or '2013' in the_line or '2014' not in the_line or "2012" in the_line or ",," in the_line:
			Delete_List.append(the_line)
		else:
			the_line = the_line.strip('\n')
			Line_Info = the_line.strip('\r')
			Line_Info = Line_Info.split(',')
			if '2014-0'+str(whitch_file) in Line_Info[1] and whitch_file <= 9:
				Temp_List.append(the_line)
			elif '2014-10' in Line_Info[1] and whitch_file == 10 :
				Temp_List.append(the_line)
			elif '2014/11' in Line_Info[1] and whitch_file == 11 :
				Temp_List.append(the_line)
			elif '2014/12' in Line_Info[1] and whitch_file == 12 :
				Temp_List.append(the_line)
			else :
				if '2014-01' in Line_Info[1]  or '2014/01' in Line_Info[1] :
					Except_List[0].append(the_line)
				elif '2014/1' in Line_Info[1] :
					if '2014/10' in Line_Info[1]:
						Except_List[9].append(the_line)
					elif '2014/11' in Line_Info[1]:
						Except_List[10].append(the_line)
					elif '2014/12' in Line_Info[1]:
						Except_List[11].append(the_line)
					else :
						Except_List[0].append(the_line)
				elif '2014-02' in Line_Info[1] or '2014/2' in Line_Info[1] or '2014/02' in Line_Info[1]:
					Except_List[1].append(the_line)
				elif '2014-03' in Line_Info[1] or '2014/3' in Line_Info[1] or '2014/03' in Line_Info[1]:
					Except_List[2].append(the_line)
				elif '2014-04' in Line_Info[1] or '2014/4' in Line_Info[1] or '2014/04' in Line_Info[1]:
					Except_List[3].append(the_line)
				elif '2014-05' in Line_Info[1] or '2014/5' in Line_Info[1] or '2014/05' in Line_Info[1]:
					Except_List[4].append(the_line)
				elif '2014-06' in Line_Info[1] or '2014/6' in Line_Info[1] or '2014/06' in Line_Info[1]:
					Except_List[5].append(the_line)
				elif '2014-07' in Line_Info[1] or '2014/7' in Line_Info[1] or '2014/07' in Line_Info[1]:
					Except_List[6].append(the_line)
				elif '2014-08' in Line_Info[1] or '2014/8' in Line_Info[1] or '2014/08' in Line_Info[1]:
					Except_List[7].append(the_line)
				elif '2014-09' in Line_Info[1] or '2014/9' in Line_Info[1] or '2014/09' in Line_Info[1]:
					Except_List[8].append(the_line)
				elif '2014-10' in Line_Info[1] or '2014/10' in Line_Info[1]:
					Except_List[9].append(the_line)
				elif '2014-11' in Line_Info[1] or '2014/11' in Line_Info[1]:
					Except_List[10].append(the_line)
				elif '2014-12' in Line_Info[1] or '2014/12' in Line_Info[1]:
					Except_List[11].append(the_line)
				else :
					Check_List.append(the_line)
					
					
				
				
	inFile.close()
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')
	newFolder = "OpenData_Clean"
	if not os.path.exists(newFolder):
		os.makedirs(newFolder)
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean')
	outFile = open(filename,'a')
	for the_line in Temp_List :
		outFile.write(the_line)
		outFile.write('\n')
	outFile.close()
	
	outFile = open('Del'+str(whitch_file).rjust(2,'0')+'.csv','a')
	for the_line in Delete_List:
		outFile.write(the_line)
	outFile.close()
	
	
	whitch_file += 1
	
	
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean')
print(len(Except_List))

print('start to check')

for index in range(0,12):
	outFile = open(FileName_List[index],'a+')
	for the_line in Except_List[index]:
		outFile.write(the_line)
		outFile.write('\n')
	outFile.close()
		

outFile = open('Check_List.csv','a+')

for element in Check_List:
	outFile.write(element)
	outFile.write('\n')
outFile.close()