# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

class BasePacket:
    def __init__(self):
        self.StartNode = ''
        self.EndNode = ''
        self.PacketType = 0
        self.Data = ''
        self.DataLength = 0
        self.SignInfo = ''
        
    def GetPacketType(self):
        return str(self.PacketType)
        
    def PacketToStr(self): 
        self.DataLength = len(self.Data)
        self.PacketStr = self.StartNode+'#'+self.EndNode+'#'+str(self.PacketType)+'#'+self.Data+"#"+str(self.DataLength)+"#"+self.SignInfo
        #self.PacketStr = ''.join(self.PacketStr.split())  #如果去除空格，将使时间出错
        return self.PacketStr
        
    def StrToPacket(self,packetStr):
         if self.IsPacket(packetStr):
             infos=str(packetStr).replace("b'","").replace("'","").split('#')
             self.StartNode = infos[0]
             self.EndNode = infos[1]
             self.PacketType=int(infos[2])
             self.Data=infos[3]
             self.DataLength=int(infos[4])
             self.SignInfo=infos[5]
             return True
         else:
             return False
        
    def IsPacket(self,packetStr): 
        temp=str(packetStr).replace("b'","").replace("'","").split('#')
        if len(temp)==6:
             return True
        return False
        
