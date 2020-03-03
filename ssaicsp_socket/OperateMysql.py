# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

import MySQLdb

class OperateMysql():
    def __init__(self,user='root',passwd='toor',database='ssaicsp',host='127.0.0.1',port=3306):
        self.User=user
        self.Passwd=passwd
        self.Database=database
        self.Host=host
        self.Port=port
        self.InitConnect() 
        pass
    def InitConnect(self):
        self.con=MySQLdb.connect(user=self.User,passwd=self.Passwd,database=self.Database,host=self.Host,port=self.Port)
        self.con.autocommit(True)#设置自动提交，避免缓存
        self.cur=self.con.cursor()
        pass
    def ReleaseConnect(self):
        self.cur.close()
        self.con.close()
        pass
    def GetData(self,sqlstr): 
        self.cur.execute(sqlstr)
        data=self.cur.fetchall() 
        return data
    def SaveData(self,sqlstr): 
        try: 
            #print("SaveData before initconnect iiiiiiiiiiii")
            self.InitConnect()
            #print("SaveData before execute  eeeeeeeeee")
            self.cur.execute(sqlstr)
            #print("SaveData before commit cccccccccc")
            self.con.commit() 
            #print("SaveData before ReleaseConnect rrrrrrrrrr")
            self.ReleaseConnect()
        except Exception as e: 
            #print("SaveData before rollback rbrbrbrbrbrbrbrbrbrb")
            self.con.rollback()
            #print("SaveData before ReleaseConnect rcrcrcrcrcrcrcrcrcrc")
            self.ReleaseConnect()
            pass
    def Execute(self,sqlstr,data):
        try: 
            self.cur.execute(sqlstr)
            self.con.commit() 
        except Exception as e: 
            pass
