# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

class InformPacket:
    def __init__(self):
        self.ControlName = 0
        self.SensorType = 0
        self.SensorCode = ''
        self.ControlStatus = ''
        self.ControlMsg = ''

    def PacketToStr(self): 
        self.PacketStr = str(self.ControlName)+'*'+str(self.SensorType)+'*'+str(self.SensorCode)+'*'+str(self.ControlStatus)+"*"+str(self.ControlMsg)
        #self.PacketStr = ''.join(self.PacketStr.split())  #如果去除空格，将使时间出错
        return self.PacketStr
        
    def StrToPacket(self,packetStr):
         if self.IsPacket(packetStr):
             infos=str(packetStr).split('*')
             self.ControlName = int(infos[0])
             self.SensorType = int(infos[1])
             self.SensorCode = infos[2]
             self.ControlStatus = infos[3]
             self.ControlMsg = infos[4]
             return True
         else:
             return False
        
    def IsPacket(self,packetStr): 
        temp=str(packetStr).split('*')
        if len(temp)==5:
             return True
        return False
        
