# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from OperateMysql import *
import random
import time
import datetime

class soil():

    def __init__(self):
        self.Context=OperateMysql()
        
    def ReadToMysql(self):#读取距离并存入数据库
        sqlStr=("INSERT INTO learn_soil(sensor_code, is_soil, soil_value, create_time, status) VALUES('{0}',{1},{2},'{3}',{4})".format('101',random.randint(0,99),random.uniform(1,99),datetime.datetime.now(),0))
        self.Context.SaveData(sqlStr)
        pass

sol = soil()
index = 1
while True:
	sol.ReadToMysql()
	print("index:"+str(index)+"  time: " +str(datetime.datetime.now()))
	index = index + 1
	time.sleep(0.01)



        
