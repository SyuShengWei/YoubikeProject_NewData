import os 
import calendar
from Function_readData import *
#Weather Data
class WeatherData :

	def __init__(self,dataList) :
		self.dataList = dataList
	
	def getList (self):
		return self.dataList
class WeatherDataLine :
	
	def __init__(self,startTime,endTime,precp,precpTime):
		self.startTime = startTime
		self.endTime = endTime
		self.precp = precp
		self.precpTime = precpTime
#
Weather_Dic ={}
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/WeatherData'):
	os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/WeatherData')
	weather_data_line = list()
	
	Data_List = list()
	readData(Data_List,filename,1)
	for the_line in Data_List:
		Line_Info = the_line.split(',')
		data_line = WeatherDataLine(Line_Info[0],Line_Info[1],Line_Info[2],Line_Info[3])
		weather_data_line.append(data_line)
	weatherData = WeatherData(weather_data_line)
	new_Dic = {filename.strip('.csv'):weatherData}
	Weather_Dic.update(new_Dic)
'''	
print(Weather_Dic['2014-01-01'].dataList[0].endTime)
'''
#Holiday Data		
Holiday_List = list()
filename = 'C:/Users/SyuShengWei/Desktop/NewDataProject/Holiday.txt'
readData(Holiday_List,filename,0)
#Station Data 
Station_Dic = {}
filename = 'C:/Users/SyuShengWei/Desktop/NewDataProject/StationData/Station_Num_222.txt'
Data_List = list()
readData(Data_List,filename,1)
for the_line in Data_List:
	Line_Info = the_line.split(',')
	new_Dic = {Line_Info[1]:Line_Info[0]}
	Station_Dic.update(new_Dic)
Data_List.clear()
#open the clean open data and record the form I want
#the data order is 1. rent date 2014-OO-XX 		2. rent time (in second) 
#				   3. return date 2014-OO-XX 	4. return time (in second)
#				   5. rent station (O)     		6. return station (D)
#				   7. week day (sun 7, mon 1 ....)	8. Holiday ? (T->1/F->0)
#				   9. rain ?(T/F)				10.how much rain (mm)
#				   11.travelTime(in second)
Exception_List = list()
Not_Station_List = list()

for folder in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_SplitByDay'):
	for filename in os.listdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_SplitByDay/'+folder):
		os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_SplitByDay/'+folder)
		Out_File_Info = list()
		File_Data = list()
		
		readData(File_Data,filename,0)
		for the_line in File_Data:
			the_info_line = ''
			
			Line_Info = the_line.split(',')
			#rent
			Rent_Info = Line_Info[1].split(' ')
			#1.rent_date (rent_weekday)
			
			try:
				if '2014-' in Rent_Info[0] :
					rent_date = Rent_Info[0]
					Rent_Date = Rent_Info[0].split('-')
					rent_weekday = calendar.weekday(int(Rent_Date[0]),int(Rent_Date[1]),int(Rent_Date[2])) + 1
				elif '2014/' in Rent_Info[0]:
					Rent_Date = Rent_Info[0].split('/')
					rent_weekday = calendar.weekday(int(Rent_Date[0]),int(Rent_Date[1]),int(Rent_Date[2])) + 1
					rent_date = Rent_Date[0] + '-' + Rent_Date[1].rjust(2,'0') + '-' + Rent_Date[2].rjust(2,'0')
				elif '2015-' in Rent_Info[0] :
					rent_date = Rent_Info[0]
					Rent_Date = Rent_Info[0].split('-')
					rent_weekday = calendar.weekday(int(Rent_Date[0]),int(Rent_Date[1]),int(Rent_Date[2])) + 1
				elif '2015/' in Rent_Info[0]:
					Rent_Date = Rent_Info[0].split('/')
					rent_weekday = calendar.weekday(int(Rent_Date[0]),int(Rent_Date[1]),int(Rent_Date[2])) + 1
					rent_date = Rent_Date[0] + '-' + Rent_Date[1].rjust(2,'0') + '-' + Rent_Date[2].rjust(2,'0')
				the_info_line += rent_date + ','
			except:
				Exception_List.append(the_line)
				print('Error :rent_date')
				#print(the_line)
				continue
			#2.rent_time
			try:
				Rent_Time_Data = Rent_Info[1].split(':')
				rent_time = int(Rent_Time_Data[0][0:2])*60*60 + int(Rent_Time_Data[1][0:2])*60 + int(Rent_Time_Data[2][0:2])
				the_info_line += str(rent_time) + ','
			except :
				Exception_List.append(the_line)
				print('Error :rent_time')
				continue
			#3.return_date
			Return_Info = Line_Info[3].split(' ')
			try:
				if '2014-' in Return_Info[0] :
					return_date = Return_Info[0]
					Return_Date = Return_Info[0].split('-')
					rent_weekday = calendar.weekday(int(Return_Date [0]),int(Return_Date [1]),int(Return_Date [2])) + 1
				elif '2014/' in Return_Info[0]:
					Return_Date  = Return_Info[0].split('/')
					rent_weekday = calendar.weekday(int(Return_Date [0]),int(Return_Date [1]),int(Return_Date [2])) + 1
					return_date = Return_Date [0] + '-' + Return_Date [1].rjust(2,'0') + '-' + Return_Date [2].rjust(2,'0')
				elif '2015-' in Return_Info[0] :
					return_date = Return_Info[0]
					Return_Date  = Return_Info[0].split('-')
					rent_weekday = calendar.weekday(int(Return_Date [0]),int(Return_Date [1]),int(Return_Date [2])) + 1
				elif '2015/' in Return_Info[0]:
					Return_Date  = Return_Info[0].split('/')
					rent_weekday = calendar.weekday(int(Return_Date [0]),int(Return_Date [1]),int(Return_Date [2])) + 1
					return_date = Return_Date [0] + '-' + Return_Date [1].rjust(2,'0') + '-' + Return_Date [2].rjust(2,'0')
				the_info_line += return_date + ','
			except:
				Exception_List.append(the_line)
				print('return_date')
				continue
			#4return_time
			try:
				Return_Time_Info = Return_Info[1].split(':')
				return_time = int(Return_Time_Info[0][0:2])*60*60 + int(Return_Time_Info[1][0:2])*60 + int(Return_Time_Info[2][0:2]) 
				the_info_line += str(return_time) + ','
			except:
				Exception_List.append(the_line)
				print('return_time')
				continue
			#5.rent_station
			try:
				if Line_Info[2] not in Station_Dic : 
					Not_Station_List.append(the_line)
					continue
				else:
					rent_station = Station_Dic[Line_Info[2]]
					the_info_line += rent_station + ','
			except:
				Exception_List.append(the_line)
				print('Error : Station')
				continue
			#6. return_station
			try:
				if Line_Info[4] not in Station_Dic : 
					Not_Station_List.append(the_line)
					continue
				else:
					return_station = Station_Dic[Line_Info[4]]
					the_info_line += return_station + ','
			except:
				Exception_List.append(the_line)
				print('Error : Station')
				continue
			#7 rent_weekday --> done at 1/F-
			the_info_line += str(rent_weekday) +','
			#8 if_holiday
			try:
				if rent_date in Holiday_List :
					if_holiday = '1'
				else:
					if_holiday = '0'
				the_info_line += if_holiday + ','
			except:
				Exception_List.append(the_line)
				print('holiday')
				continue
			#9 if_rain? 
			#10 precpMM
			try:
				weather = Weather_Dic[filename.strip('.csv')]
				for element in weather.dataList :
					if rent_time in range(int(element.startTime),int(element.endTime)):
						if element.precp != '0.0' :   
							if_rain = '1' 
							precpMM = element.precp
						else :
							if_rain = '0'
							precpMM = '0.0'
				
				the_info_line += if_rain + ',' + precpMM + ','
			except:
				Exception_List.append(the_line)
				print('rain')
				continue
			#11 travel_time
			try:
				Travel_Time_Info = Line_Info[5].split(':')
				travle_time =  int(Travel_Time_Info[0][0:2])*60*60 + int(Travel_Time_Info[1][0:2])*60 + int(Travel_Time_Info[2][0:2])
				the_info_line += str(travle_time) + '\n'
			except:	
				Exception_List.append(the_line)
				print('travel time')
				continue
			#merge data
			Out_File_Info.append(the_info_line)
		
		os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject')
		if not os.path.exists('OpenData_RegularForm'):
			os.makedirs('OpenData_RegularForm')
		os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm')
		outFile = open(filename,'a')
		outFile.write('rent date,rent time,return date,return time,rent station (O),return station (D),week day,Holiday,Rain,precp(mm),travelTime \n')
		for the_line in Out_File_Info:
			outFile.write(the_line)
		outFile.close()
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject/OpenData_RegularForm')
outFile = open('except.csv','a+')
for element in Exception_List :
	outFile.write(element)
	outFile.write('\n')
outFile.close()

outFile = open('not_station.csv','a+')
for element in Not_Station_List :
	outFile.write(element)
	outFile.write('\n')
outFile.close()

			