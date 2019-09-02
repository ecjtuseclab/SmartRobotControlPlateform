# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from Sensor import *

class ultrasonic(Sensor):
    # Trig_Pin = self.Pins[0]
    # Echo_Pin = self.Pins[1]
     def __init__(self, sensorType = 0, sensorcode = '', pins = '0', parameters = ''):
         #调用父类的构函
         Sensor.__init__(self, sensorType, sensorcode, pins, parameters)
        
     def SetupGPIO(self):
        GPIO.setup(self.Pins[0], GPIO.OUT, initial = GPIO.LOW)
        GPIO.setup(self.Pins[1], GPIO.IN)

     #读取距离
     def Read(self):
        self.Values.clear()
        Trig_Pin = self.Pins[0]
        Echo_Pin = self.Pins[1]

        GPIO.output(Trig_Pin, GPIO.HIGH)
        time.sleep(0.00015)
        GPIO.output(Trig_Pin, GPIO.LOW)
        
        while not GPIO.input(Echo_Pin):
            pass
        t1 = time.time()
        while GPIO.input(Echo_Pin):
            pass
        t2 = time.time()
        self.Values.append((t2-t1)*340*100/2)
        
     def GetSqlStr(self):
        value0 = "INSERT INTO ssaicsp_ultrasonic(sensor_code,distance,create_time,status) VALUES"
        value1 = "({0},{1},'{2}',0),".format(self.SensorCode,self.Values[0],datetime.datetime.now())
        return value0,value1


