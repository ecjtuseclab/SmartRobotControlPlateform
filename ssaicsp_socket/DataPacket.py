# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

class DataPacket:
    def __init__(self):
        self.SensorType = 0
        self.SensorData = ''
        
    def GetKey(self):
        return str(self.SensorType)
        
    def PacketToStr(self): 
        self.DataLength = len(self.SensorData)
        self.PacketStr = str(self.SensorType)+'*'+str(self.SensorData)
        #self.PacketStr = ''.join(self.PacketStr.split())  #如果去除空格，将使时间出错
        return True
        
    def StrToPacket(self,packetStr):
         if self.IsPacket(packetStr):
             infos=str(packetStr).split('*')
             self.SensorType = int(infos[0])
             self.SensorData = infos[1]
             return True
         else:
             return False
        
    def IsPacket(self,packetStr): 
        temp=str(packetStr).split('*')
        if len(temp) == 2:
             return True
        return False
        
        
