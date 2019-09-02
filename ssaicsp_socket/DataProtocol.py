# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from  DataPacket import *
from  OperateMysql import *
from  RedisDic import *

class DataProtocol():
    
    sensors={1:'learn_activebuzzer',2:'learn_aroadtracing',3:'learn_dht11',
             4:'learn_fire',5:'learn_human',6:'learn_infraredemission',7:'learn_infraredreception',
             8:'learn_light',9:'learn_obstacleavoidance',10:'learn_rain',11:'learn_smoke',
             12:'learn_soil',13:'learn_sound',14:'learn_ultrasonic'}
             
    def __init__(self):
        self.Redis = RedisDict()
        pass
    
    def GetDataPacket(self,sType):       
        self.Redis.sensortype = str(sType)
        
        datapacket = DataPacket()
        datapacket.SensorType = sType
        datapacket.SensorData = self.Redis.get("0").replace('"','')
        datapacket.PacketToStr()
        
        if datapacket.DataLength > 0:  #如果传感器有值，则返回二级封包
            self.Redis.pop("0")
            return datapacket.PacketStr
        else:
            return''
        
    def UpdateStatus(self,inpacket): 
         sqlStr='UPDATE {0} SET status=1 WHERE id in ({1})'.format(self.sensors[inpacket.SensorType],inpacket.Data) 
         print(sqlStr) 
         self.Context.SaveData(sqlStr);
         pass          
             
    '''
    def __init__(self):
        self.Context=OperateMysql()
        pass
    def GetDataPacket(self,sType):
        sqlStr='SELECT  * FROM {0}  WHERE status=0 LIMIT 0,5'.format(self.sensors[sType]) 
        dataStr=''
        data=self.Context.GetData(sqlStr)
        for Item in data:
            dataStr=dataStr+'_'+str(Item)
        
        datapacket = DataPacket()
        datapacket.SensorType = sType
        datapacket.ControlData =dataStr
        datapacket.PacketToStr()
        
        return datapacket.PacketStr
        
    def UpdateStatus(self,inpacket): 
         sqlStr='UPDATE {0} SET status=1 WHERE id in ({1})'.format(self.sensors[inpacket.SensorType],inpacket.Data) 
         print(sqlStr) 
         self.Context.SaveData(sqlStr);
         pass
    '''
        
            
