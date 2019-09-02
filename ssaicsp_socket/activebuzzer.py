# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from Sensor import *
from gpiozero import Buzzer

class activebuzzer(Sensor):
     def __init__(self, sensorType = 0, sensorcode = '', pins = '0', parameters = ''):
         #调用父类的构函
         Sensor.__init__(self, sensorType, sensorcode, pins, parameters)
         
     def GetSqlStr(self):
        value0 = "INSERT INTO ssaicsp_activebuzzer(sensor_code,is_activebuzzer,create_time,status) VALUES"
        value1 = "({0},{1},'{2}',0),".format(self.SensorCode,self.Values[0],datetime.datetime.now())
        return value0,value1
        
     def SetupGPIO(self):
        for pin in self.Pins:
            GPIO.setup(pin, GPIO.OUT)
            
     def Read(self):
        self.Values.clear()
        for pin in self.Pins:
            bz=Buzzer(pin)   
            #beep(on_time=1,off_time=1,n=None,background=Ture) 
            bz.beep(1,0.1,1,False)
            self.Values.append(1)

