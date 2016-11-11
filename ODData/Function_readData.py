def readData (Storage_List , filename ,if_title_line = 0):
	inFile = open(filename,'r')
	if if_title_line != 0 :
		title_line = inFile.readline()
	
	Data_List = inFile.readlines()
	for the_line in Data_List :
		the_line = the_line.strip('\n')
		Storage_List.append(the_line)
	inFile.close()