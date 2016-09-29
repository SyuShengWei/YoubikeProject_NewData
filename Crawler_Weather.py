import os 
import urllib.request
import urllib
from urllib.request import urlopen

os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')

Day_List = list()
inFile = open('DayList.txt','r')
Data = inFile.readlines()
for line in Data:
	the_line = line.strip('\n')
	Day_List.append(the_line)

for the_day in Day_List:
	
	url = 'http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466920&stname=%25E8%2587%25BA%25E5%258C%2597&datepicker=' + the_day

	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	data = response.read()
	data_theline = data.decode()
	Data_Line = data_theline.split('\n')

	outList = list()

	for i in range(0,len(Data_Line)) :

		if '<tr class="second_tr">' in Data_Line[i]:
			out_line = '觀察開始,'
			for index in range(0,15):
				line = Data_Line[i+1+index].replace('\t','')
				line = line.replace('<th>','')
				line = line.replace('</th>','')
				line = line.replace('<br>','')
				line = line.replace('\r','')
				out_line += line 
				if index != 14:
					out_line += ','
				else: 
					out_line += '\n'
			outList.append(out_line)
	
		if '<td nowrap' in Data_Line[i]:
			line_title = Data_Line[i].replace('<td nowrap','')
			line_title = line_title.replace('</td>','')
			line_title = line_title.replace('>','')
			line_title = line_title.replace('\t','')
			line_title = line_title.replace('\r','')
			start_time = int(line_title) -1
			out_line = str(start_time) + ',' + line_title + ','
			for index in range(0,14):
				line = Data_Line[i+1+index].replace('\t','')
				line = line.replace('<td>','')
				line = line.replace('&nbsp;</td>','')
				line = line.replace('\r','')
				if line == '' : 
					out_line += 'non'
				else :
					out_line += line 
				if index != 13:
					out_line += ','
				else: 
					out_line += '\n'
			outList.append(out_line)
	'''
	if not os.path.exists('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Weather'):
		os.makedirs('OpenData_Weather')
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_Weather')
	
	outFile = open(the_day + '.csv','a')
	for data in outList :
		outFile.write(data)
	outFile.close()
	'''
