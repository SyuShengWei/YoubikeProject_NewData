import os

NUM_STATION = 196

class CDF :
	#member data
	dataList = list()
	len_of_list = len(dataList)
	probability_of_each_test = 0
	#initialization function
	
	
	def __init__(self,dataList):
		self.dataList = dataList
		self.len_of_list = len(dataList)
	#call:CDF.prob_within_X(x,precise) x is the input value ,precise is the round of digit
	def prob_within_X(self,X_value,precise = 2):
		testList = list()
		testList = list(self.dataList) 
		testList.append(X_value)
		testList.sort()
		len_of_test = len(testList)
		probability_of_each_test = round(1/len_of_test,precise)
		probList = list()
		for i in range(0,len_of_test,1):
			probList.append((i+1) * probability_of_each_test)
		for i in range(len_of_test - 1,-1,-1):
			if testList[i] == X_value:
				probIndex = i
				break
		if probList[probIndex] > 1 :
			probList[probIndex] = 1
		return probList[probIndex]
	
def TravelingTime_CDF(O_station,D_station,X_value,precise = 10):

	if O_station not in range(0,NUM_STATION) or D_station not in range(0,NUM_STATION):
		print('wrong input , please try again')
		return
	theCDF = CDF(TravelingTimeDataMatrix[O_station][D_station])
	the_probability = theCDF.prob_within_X(X_value,precise)
	return the_probability



TravelingTimeDataMatrix = list()
for i in range (0,NUM_STATION):
	distinationList = list()
	for j in range(0,NUM_STATION):
		eachKindDataList = list()
		distinationList.append(eachKindDataList)
	TravelingTimeDataMatrix.append(distinationList)
#input data

print('Reading InFile')
os.chdir('C:/Users/SyuShengWei/Desktop/NewDataProject') #you can change you path here
inFile = open('CDF_Data_Normalday.txt','r')
theData = inFile.readlines()
for i in range(0,len(theData)):
	OIndex = int(i / NUM_STATION)
	DIndex = i % NUM_STATION
	OD_Data = theData[i].strip('\n') 
	OD_Data = OD_Data.split(',')
	if '' in OD_Data : continue
	else: 
		for element in OD_Data :
			TravelingTimeDataMatrix[OIndex][DIndex].append(int(element))
inFile.close()

