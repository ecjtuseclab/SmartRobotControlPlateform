# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from Sensor import *
from gpiozero import PWMLED

class led(Sensor):
     def __init__(self, sensorType = 0, sensorcode = '', pins = '0', parameters = ''):
         #调用父类的构函
         Sensor.__init__(self, sensorType, sensorcode, pins, parameters)
         for pin in self.Pins:
             self.led = PWMLED(pin)   
        
     def SetupGPIO(self):
        for pin in self.Pins:
            GPIO.setup(pin, GPIO.OUT)
        pass
            
     def ReadToCache(self):
        self.Values.clear()
        for pin in self.Pins:
            value = float(self.Parameters[0])
            self.led.value = value
            self.Values.append(value)
            
        #将采集到的数据存入redis缓存
        self.SetCache()
        print('ReadToCache', datetime.datetime.now(), self.GetKey(), self.Pins, self.Values, self.Redis.GetCount(self.SensorCode))
        pass
    
     def GetSqlStr(self):
        value0 = "INSERT INTO learn_led(sensor_code,is_led,create_time,status) VALUES"
        value1 = "({0},{1},'{2}',0),".format(self.SensorCode,self.Values[0],datetime.datetime.now())
        return value0,value1

     def Stop(self):
        self.Values.clear()
        for pin in self.Pins: 
            self.led.off()
            self.Values.append(0)
            
     def SensorControllerSpecial(self,spacket):
        try:
            flag = False
            if spacket.ControlName == 11:   #开灯并调节亮度
                flag = self.ReSet(spacket.SensorPins, spacket.ControlData)
                print('重置传感器',flag)
            elif spacket.ControlName == 12:   #调节亮度
                print('调节亮度',spacket.ControlData)
                self.led.value = float(spacket.ControlData)
                flag = True
            else:
                print('无此命令')
            return flag
            
        except Exception as e:
            return False

            
  









            
            
            
            