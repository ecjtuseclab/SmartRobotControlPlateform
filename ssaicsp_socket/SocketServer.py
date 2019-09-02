# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""
 
import socket

class SocketServer: 
    #构造函数
    def __init__(self,host,port,maxconn):
        
        self.Host=host
        self.Port=port
        self.Maxconn=maxconn #最大连接数量

        self.server=socket.socket()
        self.server.bind((self.Host,self.Port))
        self.server.listen(self.Maxconn)
    
  