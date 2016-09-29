import os 

Except_List = list()

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean'):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Clean')
	
	Day_List = list()
	for i in range(0,31):
		Data_List = list()
		Day_List.append(Data_List)
	
	inFile = open(filename,'r')
	Data_List = inFile.readlines()
	for the_line in Data_List :
		Line_Info = the_line.split(',')
		if '2014-' in Line_Info[1] :
			Rent_Data_Info = Line_Info[1].split(' ')
			day_info = Rent_Data_Info[0].split('-')
			day_index = int(day_info[2]) -1
			Day_List[day_index].append(the_line)
		elif '2014/' in Line_Info[1] :
			Rent_Data_Info = Line_Info[1].split(' ')
			day_info = Rent_Data_Info[0].split('/')
			day_index = int(day_info[2]) -1
			Day_List[day_index].append(the_line)
		elif '2015-' in Line_Info[1] :
			Rent_Data_Info = Line_Info[1].split(' ')
			day_info = Rent_Data_Info[0].split('-')
			day_index = int(day_info[2]) -1
			Day_List[day_index].append(the_line)
		elif '2015/' in Line_Info[1] :
			Rent_Data_Info = Line_Info[1].split(' ')
			day_info = Rent_Data_Info[0].split('/')
			day_index = int(day_info[2]) -1
			Day_List[day_index].append(the_line)
		else:
			Except_List.append(the_line)
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')
	if not os.path.exists('OpenData_SplitByDay'):
		os.makedirs('OpenData_SplitByDay')
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_SplitByDay')
	if not os.path.exists(filename.strip('.csv')):
		os.makedirs(filename.strip('.csv'))
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_SplitByDay/'+filename.strip('.csv'))
	
	for index in range(0,31):
		if len(Day_List[index]) == 0:
			continue
		else:
			day = index + 1
			file = filename.strip('.csv')
			outFile = open(file[0:4] + '-' +file[4:6] + '-' + str(day).rjust(2,'0') + '.csv' ,'a')
			for the_line in Day_List[index] :
				outFile.write(the_line)
			outFile.close()

print('output except')
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')
outFile = open('Except_SplitByDay.csv','a+')
for element in Except_List :
	outFile.write(element)
outFile.close()