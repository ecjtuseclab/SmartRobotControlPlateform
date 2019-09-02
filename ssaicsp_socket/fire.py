# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from Sensor import *

class fire(Sensor):
     def __init__(self, sensorType = 0, sensorcode = '', pins = '0', parameters = ''):
         #调用父类的构函
         Sensor.__init__(self, sensorType, sensorcode, pins, parameters)

     def GetSqlStr(self):
        value0 = "INSERT INTO ssaicsp_fire(sensor_code,is_fire,fire_value,create_time,status) VALUES"
        value1 = "({0},{1},{2},'{3}',0),".format(self.SensorCode,self.Values[0],self.Values[1],datetime.datetime.now())
        return value0,value1
