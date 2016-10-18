import Function_readData as RD
import Function_readStationOD as RSOD

Normalday_List = list()
RD.readData(Normalday_List,'C:/Users/SyuShengWei/Desktop/NewDataProject/Normalday.txt')

List = [1,2,3]

RSOD1 = RSOD.ReadStationOD.passList(List)
RSOD1.printit()

RSOD2 = RSOD.ReadStationOD.createNew(213,48,'C:/Users/SyuShengWei/Desktop/NewDataProject/OD_Record_byStation/000',Normalday_List)
RSOD2.printit()
#Station_OD.printDayRecord(15)