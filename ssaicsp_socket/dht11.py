# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from Sensor import *

class dht11(Sensor):
     def __init__(self, sensorType = 0, sensorcode = '', pins = '0', parameters = ''):
         #调用父类的构函
         Sensor.__init__(self, sensorType, sensorcode, pins, parameters)
    
     def ReadFor(self):
        data = [] #温湿度值	
        j = 0
        time.sleep(0.15)
        Channel = self.Pins[0]
        #开始握手	
        GPIO.setup(Channel, GPIO.OUT)
        GPIO.output(Channel, GPIO.LOW)
        time.sleep(0.02)
        GPIO.output(Channel, GPIO.HIGH)
        GPIO.setup(Channel, GPIO.IN)	
        
        while GPIO.input(Channel) == GPIO.LOW: 	
            continue
        
        while GPIO.input(Channel) == GPIO.HIGH:
            continue
    
        while j < 40:
            k = 0	
            while GPIO.input(Channel) == GPIO.LOW: 	
                continue
            
            while GPIO.input(Channel) == GPIO.HIGH:
                k += 1	
                if k > 100:	
                    break	
                
            if k < 8:	
                data.append(0)
            else:
                data.append(1)
        
            j += 1 #输出初始数据高低电平
         
        humidity_bit = data[0:8] #分组	
        humidity_point_bit = data[8:16]
        temperature_bit = data[16:24]
        temperature_point_bit = data[24:32]
        check_bit = data[32:40]

        humidity = 0
        humidity_point = 0
        temperature = 0
        temperature_point = 0
        check = 0 
        
        for i in range(8):
            humidity += humidity_bit[i] * 2 ** (7 - i)
            humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
            temperature += temperature_bit[i] * 2 ** (7 - i)
            temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
            check += check_bit[i] * 2 ** (7 - i)

            
        tmp = humidity + humidity_point + temperature + temperature_point		#十进制的数据相加
        result=False

        if check == tmp:  #数据校验，相等则输出		
            self.Values.clear()
            self.Values.append(float(str(temperature)+'.'+str(temperature_point)))
            self.Values.append(float(str(humidity)+'.'+str(humidity_point)))
            result = True
        else:  #错误输出错误信息，和校验数据		
            result = False
            
        return result 
    
     def Read(self):
         index = 0
         flag = False
         
         while  not flag:
            flag =self.ReadFor() #并且将数据插入到数据库中
            index += 1
            if index == 50:
                flag = True
 
     def GetSqlStr(self):
        value0 = "INSERT INTO learn_dht11(sensor_code,temperature,humidity,create_time,status) VALUES"
        value1 = "({0},{1},{2},'{3}',0),".format(self.SensorCode,self.Values[0],self.Values[1],datetime.datetime.now())
        return value0,value1



        



