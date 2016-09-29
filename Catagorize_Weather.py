import os 
import codecs

'''
data form  1. start time (0) 2. end time (1) 3. how much rain (11)
'''


whichFile = 1

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Weather'):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Weather')
	
	print('File is : '+ str(whichFile) )
	
	Data_Line_List = list()
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	Data = inFile.readlines()
	ctr = 0
	
	for theLine in Data:
		
		Data_Element_List = list()
		
		ctr += 1
		lineInfo = theLine.split(',')
		#時段
		timeStart 	= int(lineInfo[0]) *60 *60
		timeEnd 	= int(lineInfo[1])	*60 *60
		Data_Element_List.append(str(timeStart))
		Data_Element_List.append(str(timeEnd))
		#雨量
		Data_Element_List.append(lineInfo[11])
		#下雨小時
		Data_Element_List.append(lineInfo[12])
		#氣溫
		Data_Element_List.append(lineInfo[4])
		#outline
		out_line = ''
		for i in range(0,len(Data_Element_List)):
			out_line += Data_Element_List[i]
			if i != len(Data_Element_List) -1 : out_line += ','
			else: out_line += '\n'

		Data_Line_List.append(out_line)
		
	#print(Data_Line_List)
	#print(len(Data_Line_List))
	if ctr != 24 :
		print('error file = ' + str(whichFile) + ' with line : ' + str(ctr) )
	
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/')
	if not os.path.exists('WeatherData'):
		os.makedirs('WeatherData')
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/WeatherData')
	
	outFile = open(filename,'a')
	outFile.write('StartTime,EndTime,Precp(mm),PrecpHour(hr),Tempture(C) \n ')
	for element in Data_Line_List :
		outFile.write(str(element))
	outFile.close()
	whichFile += 1
	