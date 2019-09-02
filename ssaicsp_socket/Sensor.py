# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""


import RPi.GPIO as GPIO
import time
from threading import Timer
import datetime
import random
from RedisDic import *

class Sensor:
    ReadTimer_interval = 5#采集频率
    Pins = [] #引脚号4
    Values = [] #引脚号对应的信号值
    SensorCode = 0
    SensorType = 0
    RedisCount = 10
    Enable = 1
    Parameters = []
         
    #初始化方法
    def __init__(self, sensorType = 0, sensorcode = '', pins = '0', controldata = ''):
        # ControlData = str(enable)+','+str(acqfre)+','+str(rediscount)+','+str(parameters)
        # Data = '2*'+str(type)+'*'+str(sensor_code)+'*'+str(pins)+'*'+ControlData
        param = self.GetControlData(controldata)
        self.SensorType = int(sensorType)
        self.SensorCode = sensorcode
        
        self.Enable = int(param[0])
        self.ReadTimer_interval = float(param[1])
        self.RedisCount = int(param[2])
        self.Parameters = self.SetParameters(param[3])
        self.Pins = self.GetPins(pins)
        
        self.Redis = RedisDict()   
        self.Redis.sensortype = str(self.SensorType)
        self.Redis.count = self.RedisCount
        self.Redis.pop(self.SensorCode)
        
        self.readTimer=Timer(self.ReadTimer_interval, self.ReadToCache)
        self.InitGPIO()
        
    def GetPins(self,str_pins):
        str_pins = ''.join(str_pins.split())
        confs = str_pins.split(',')
        pins = list(map(int,confs))
        return pins
        
    def GetControlData(self,str_data):
        str_data = ''.join(str_data.split())
        data = str_data.split(',')
        return data
    
    #初始化GPIO
    def InitGPIO(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)	#以BCM编码格式 		
        self.SetupGPIO()
        #time.sleep(0.2)
        pass
        
    def SetupGPIO(self):
        for pin in self.Pins:
            GPIO.setup(pin, GPIO.IN)
            #self.Values.append(random.randint(1,99))
        pass
    
    def SetParameters(self,str_param):
        if str_param != 'None' and str_param != '':
            str_param = ''.join(str_param.split())
            param = str_param.split('|')
            #param = list(map(int,confs))
            return param
        else:
            return []
        
    #获得字符串
    def GetKey(self):
        return str(self.SensorType)+'_'+str(self.SensorCode)

    def Start(self):
        if self.Enable == 1:
            self.ReadToCache()
        else:
            print(self.SensorCode, '设备未启用！')

    def Read(self):
        self.Values.clear()
        for pin in self.Pins:
            self.Values.append(GPIO.input(pin))
            #self.Values.append(random.randint(1,99))
    
    def ReadToCache(self):
        self.Read()
        #将采集到的数据存入redis缓存
        self.SetCache()
        print('ReadToCache', datetime.datetime.now(), self.GetKey(), self.Pins, self.Values, self.Redis.GetCount(self.SensorCode))
        
        #如果设置了定时器，则定时器启动
        if self.ReadTimer_interval > 0:
            self.readTimer=Timer(self.ReadTimer_interval,self.ReadToCache)
            self.readTimer.start()
        pass\
        
    
    def GetSqlStr(self):
        value0 = "INSERT INTO ssaicsp_rain(sensor_code,is_rain,rain_value,create_time,status) VALUES"
        value1 = "({0},{1},{2},'{3}',0),".format(self.SensorCode,self.Values[0],self.Values[1],datetime.datetime.now())
        return value0,value1
    
    def SetCache(self):
        value = self.GetSqlStr()
        self.Redis.SetDefaultByCount(self.SensorCode, value[0], value[1])
        #同时将获取的传感器数据发送到数据中心
        self.Redis.SetDefault("0", value[1])
        #print('SetCache', self.Redis.get(self.SensorCode))
            
    def ReSet(self, pins = '0', controldata = ''):#重新设置信息
        # ControlData = str(enable)+','+str(acqfre)+','+str(rediscount)+','+str(parameters)
        # Data = '2*'+str(type)+'*'+str(sensor_code)+'*'+str(pins)+'*'+ControlData
        try:
            param = self.GetControlData(controldata)
            self.Enable = int(param[0])
            self.ReadTimer_interval = float(param[1])
            self.Pins = self.GetPins(pins)
            self.RedisCount = int(param[2])
            self.Parameters = self.SetParameters(param[3])
            
            #重置缓存信息
            self.Redis.count = self.RedisCount
            self.Redis.sensortype = self.SensorType     
            #self.Redis.pop(self.SensorCode)

            #清除Values
            self.Values.clear()
            self.InitGPIO()
    
            if self.Enable == 1:   #启动 1
                #如果设置了定时器，则定时器启动
                if self.ReadTimer_interval > 0:
                    self.readTimer.cancel()
                    self.readTimer=Timer(self.ReadTimer_interval,self.ReadToCache)
                    self.readTimer.start()
                else:
                    self.ReadToCache()
            else: #停止 0
                self.Stop()
                
            return True
        except Exception as e:
            return False
        pass

    def Stop(self):
        #print('Stop')
        self.readTimer.cancel()
        #print('Stop after')

    def SensorController(self,spacket):
        try:
            flag = False
            if spacket.ControlName == 2:   #重置传感器
                flag = self.ReSet(spacket.SensorPins, spacket.ControlData)
                print('重置传感器',flag)
            else:
                flag = self.SensorControllerSpecial(spacket)
                
            return flag
        except Exception as e:
            return False
            
    def SensorControllerSpecial(self,spacket):
        try:
            print('特别命令')
            return True
        except Exception as e:
            return False








