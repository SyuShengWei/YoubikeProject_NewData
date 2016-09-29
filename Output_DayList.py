outFile = open('C:/Users/SyuShengWei/Desktop/NewDataProject/DayList.txt','a')

year_list = [2014,2015]
for year in year_list :
	for i in range(1,13,1):
		if i == 1 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 2 :
			for j in range(1,29):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 3 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 4 :
			for j in range(1,31):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 5 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 6 :
			for j in range(1,31):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 7 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 8 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 9 :
			for j in range(1,31):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 10 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 11 :
			for j in range(1,31):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
		if i == 12 :
			for j in range(1,32):
				outFile.write(str(year) +'-'+ str(i).rjust(2,'0') + '-' + str(j).rjust(2,'0') + '\n')
outFile.close()