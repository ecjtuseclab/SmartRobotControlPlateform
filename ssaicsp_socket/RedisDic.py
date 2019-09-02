# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from redis import Redis
import datetime
import json
from OperateMysql import *
 
class RedisDict:
    def __init__(self):
        self.data = Redis(host='127.0.0.1',port=6379)
        self.sensortype = 0
        self.mysql= OperateMysql()
        self.count = 0
 
    def get(self, sensorcode):
        sensorcode = str(sensorcode)
        redis_sensorcode = str(self.sensortype) + '_' + sensorcode
        redis_val = self.data.get(redis_sensorcode)
        if redis_val is None:
            return ''
        else:
            return redis_val.decode()
            #return json.loads(redis_val)

    def set(self, sensorcode, val):
        sensorcode = str(sensorcode)
        redis_sensorcode = str(self.sensortype) + '_' + sensorcode
        redis_val = json.dumps(val)
        self.data.set(redis_sensorcode, redis_val) 

    def SetDefaultByCount(self, sensorcode, value0, value1):
        sensorcode = str(sensorcode)
        redis_sensorcode = str(self.sensortype) + '_' + sensorcode
        redis_val = self.data.get(redis_sensorcode)
        
        #print(str(redis_val).count("),"))
        
        if str(redis_val).count("),") >= self.count:
            self.pop(sensorcode)
            #插入数据库
            #print(redis_val.decode()[1:][:-2])
            self.mysql.SaveData(redis_val.decode()[1:][:-2])
            redis_val=None

        if redis_val is None:
            #print(redis_val)
            self.set(sensorcode, value0+value1)
        else:
            #print(redis_val.decode().strip('"')+value1)
            self.set(sensorcode, redis_val.decode().strip('"')+value1)
            
        return True
        
    def SetDefault(self, sensorcode, value1):
        sensorcode = str(sensorcode)
        redis_sensorcode = str(self.sensortype) + '_' + sensorcode
        redis_val = self.data.get(redis_sensorcode)
        
        if str(redis_val).count("_(") == 0:
            self.set(sensorcode, '_'+value1[:-1])
        else:
            #print(redis_val.decode().strip('"')+value1)
            self.set(sensorcode, redis_val.decode().strip('"')+'_'+value1[:-1])
            
        return True     
        
 
    def pop(self, sensorcode):
        sensorcode = str(sensorcode)
        redis_sensorcode = str(self.sensortype) + '_' + sensorcode
        self.data.delete(redis_sensorcode)
        
    def GetCount(self, sensorcode):
        sensorcode = str(sensorcode)
        redis_sensorcode = str(self.sensortype) + '_' + sensorcode
        redis_val = self.data.get(redis_sensorcode)
        return str(redis_val).count("),")

'''
if __name__ == '__main__':
    r = RedisDict('learn')
    table = 'rain'
    
    value0 = "INSERT INTO ssaicsp_rain(sensor_code,is_rain,rain_value,create_time,status) VALUES"
    value1 = "({0},{1},{2},'{3}',0),".format(2,1,1,datetime.datetime.now())
        
    r.SetDefault(table, value0, value1)
    
    #print(r.get(table))
'''


