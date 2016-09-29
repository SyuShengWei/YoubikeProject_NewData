import os
import codecs
import copy

Except_List = list()
for i in range(0,24):
	Data_List = list()
	Except_List.append(Data_List)

	
Check_List = list()

FileName_List = ['20140101~31DIGES.csv','20140201~28DIGES.csv','20140301~31DIGES.csv','20140401~30DIGES.csv','20140501~31DIGES.csv','20140601~30DIGES.csv','20140701~0731DIGES.csv','20140801~0831DIGES.csv','20140901~0930DIGES.csv','20141001~1031DIGES.csv','20141103~1130DIGES.csv','20141201~1231DIGES.csv']
FileName_List_104 = ['20150101~0131.csv','20150201~0228.csv','20150301~0331.csv','20150401~0430.csv','20150501~0531.csv','20150601~0630.csv','20150701~0731.csv','20150801~0831.csv','20150901~0930.csv','20151001~1031.csv','20151101~1130.csv','20151201~1231.csv']

FileName_List += FileName_List_104

whitch_file = 13
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/104'):
	
	print('File : '+str(whitch_file))
	Delete_List = list()
	
	Temp_List = list()
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_New/104')
	inFile = codecs.open(filename, 'r')
	Data_List = inFile.readlines()
	for the_line in Data_List :
		if '@' in the_line or '2013' in the_line  or "2012" in the_line or ",," in the_line :
			Delete_List.append(the_line)
		else:
			the_line = the_line.strip('\n')
			Line_Info = the_line.strip('\r')
			Line_Info = Line_Info.split(',')
			if '2015/0'+str(whitch_file-12) in Line_Info[1] or '2015/'+str(whitch_file-12) in Line_Info[1] and whitch_file-12 <= 9:
				Temp_List.append(the_line)
			elif '2015/10' in Line_Info[1] and whitch_file-12 == 10 :
				Temp_List.append(the_line)
			elif '2015/11' in Line_Info[1] and whitch_file-12 == 11 :
				Temp_List.append(the_line)
			elif '2015/12' in Line_Info[1] and whitch_file-12 == 12 :
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
					else:
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
				if '2015-01' in Line_Info[1]  or '2015/01' in Line_Info[1] :
					Except_List[12].append(the_line)
				elif '2015/1' in Line_Info[1] :
					if '2015/10' in Line_Info[1]:
						Except_List[21].append(the_line)
					elif '2015/11' in Line_Info[1]:
						Except_List[22].append(the_line)
					elif '2015/12' in Line_Info[1]:
						Except_List[23].append(the_line)
					else:
						Except_List[12].append(the_line)
				elif '2015-02' in Line_Info[1] or '2015/2' in Line_Info[1] or '2015/02' in Line_Info[1]:
					Except_List[13].append(the_line)
				elif '2015-03' in Line_Info[1] or '2015/3' in Line_Info[1] or '2015/03' in Line_Info[1]:
					Except_List[14].append(the_line)
				elif '2015-04' in Line_Info[1] or '2015/4' in Line_Info[1] or '2015/04' in Line_Info[1]:
					Except_List[15].append(the_line)
				elif '2015-05' in Line_Info[1] or '2015/5' in Line_Info[1] or '2015/05' in Line_Info[1]:
					Except_List[16].append(the_line)
				elif '2015-06' in Line_Info[1] or '2015/6' in Line_Info[1] or '2015/06' in Line_Info[1]:
					Except_List[17].append(the_line)
				elif '2015-07' in Line_Info[1] or '2015/7' in Line_Info[1] or '2015/07' in Line_Info[1]:
					Except_List[18].append(the_line)
				elif '2015-08' in Line_Info[1] or '2015/8' in Line_Info[1] or '2015/08' in Line_Info[1]:
					Except_List[19].append(the_line)
				elif '2015-09' in Line_Info[1] or '2015/9' in Line_Info[1] or '2015/09' in Line_Info[1]:
					Except_List[20].append(the_line)
				elif '2015-10' in Line_Info[1] or '2015/10' in Line_Info[1]:
					Except_List[21].append(the_line)
				elif '2015-11' in Line_Info[1] or '2015/11' in Line_Info[1]:
					Except_List[22].append(the_line)
				elif '2015-12' in Line_Info[1] or '2015/12' in Line_Info[1]:
					Except_List[23].append(the_line)
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

for index in range(0,24):
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