# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 01:28:41 2016

@author: SyuShengWei
"""

class RankStation :			
	def __init__ (self,station_Num,station_OD):
		#station_num is designed as list for same OD station
		self.station_num = list()
		self.station_num.append(station_Num)
		self.station_OD = station_OD
		self.station_ODR = 0.0
		
	def getNum (self):
		return self.station_num
	
	def getOD(self):
		return self.station_OD
		
	def getODR(self):
		return self.station_ODR 
	
	def setNum (self,num):
		self.station_num = num
		
	def setOD (self,OD):
		self.station_OD = OD	
	
	def setODR(self,ODR):
		self.station_ODR = ODR
	
	def insertStation(self,num):
		self.station_num.append(num)