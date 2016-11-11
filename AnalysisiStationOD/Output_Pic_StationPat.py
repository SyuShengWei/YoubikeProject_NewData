import os 
import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


infile_path  = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/ODR_byPeriod/'
outfile_path = 'C:/Users/SyuShengWei/Desktop/AnalysisiStationOD/Pic_StationPattern/'
if not os.path.exists(outfile_path):
	os.makedirs(outfile_path)

NUM_STATION = 196

for file_name in os.listdir(infile_path):

	## skip 0~6am
	if int(file_name.strip('.txt')) <= 46: continue
	## read OD record
	os.chdir(infile_path)	
	OD_Record = []	
	inFile = open (file_name)
	for Line_Info in csv.reader(inFile):
		Float_Line = []
		for element in Line_Info:
			try:
				Float_Line.append(float(element))
			except:
				print(element)
		OD_Record.append(Float_Line)
	inFile.close()
	
	## set the record into Dict
	
	for O in range(NUM_STATION):
		
		O_Record_Dic = {}
		for D in range(NUM_STATION):
			if OD_Record[O][D] == 0.0:continue
			else:
				if OD_Record[O][D] <= 0.01 : continue
				new_dic = {D:OD_Record[O][D]}
				O_Record_Dic.update(new_dic)
	##create Order Dictionary to sort the rank		
		O_Record_OrderDic =  OrderedDict(sorted(O_Record_Dic.items(),reverse=True, key=lambda t: t[1]))	
	##take out 80% data from the O_Record_OrderDic 
		OrderDic_80 = OrderedDict()
		sum_up_value = 0
		for element in O_Record_OrderDic.items():
			if sum_up_value + element[1] <= 0.80 :
				new_dic = {element[0]:element[1]}
				OrderDic_80.update(new_dic)
			else:
				break
	##draw pic and out File
		outpic_path = outfile_path + str(O).rjust(3,'0')	
		if not os.path.exists(outpic_path):
			os.makedirs(outpic_path)
		os.chdir(outpic_path)
		
		fig = plt.figure()
		pic = fig.add_subplot(111)
		xticks = np.arange(len(OrderDic_80)) + 1
		pic.barh(xticks, OrderDic_80.values(), align='center' ,color = 'g')
		pic.grid(True)	
		#plt.yticks(xticks, list(OrderDic_80.keys()))  # 預設 X 座標數字，改顯示水果名
		title_name = "Period={} Station={}".format(file_name.strip('.txt'),str(O).rjust(3,'0'))
		pic.set_title(title_name)  # 給標題
		plt.yticks(xticks, list(OrderDic_80.keys()))
		#plt.show()
		fig.savefig(title_name+'.png')
		fig.clear()
		plt.close()
		
	