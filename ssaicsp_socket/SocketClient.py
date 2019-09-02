# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""
 
import socket
import threading
class SocketClient: 
    #构造函数
    def __init__(self,host,port,mainpanel):
        self.Host=host
        self.Port=port
        self.Mainpanel=mainpanel
        self.client=socket.socket()
        #self.IsConnected = False
            
    def ConnectServer(self):
        try:
            self.client.connect((self.Host,self.Port))
            thread=threading.Thread(target=self.Client_handle)
            thread.start()
            return True
        except Exception as e:
            return False
        finally:
            pass
    def Client_handle(self):
        
        while True:
                 try:
                     #接受到的控制命令
                     data=self.client.recv(2048) 
                     if not data:
                         pass
                     else:
                     #处理封包
                         self.Mainpanel.Receive(data)
                     #返回结果
                     #连接状态为true
                 except Exception as e:
                     print("break")
                     #连接状态为false
                     break
    def SendMessage(self,messgae):
        try:
            self.client.send(messgae.encode('UTF-8'))
            #self.Receive()
            return True
        except Exception as e:
            return False
        finally:
            pass
    #def Receive(self):
      #  try:
      #      data=self.client.recv(1024)
      #      self.Mainpanel.Receive(data)
       #     return True
      #  except Exception as e:
       #     return False
      #  finally:
       #     pass
    
    def IsConnected(self):
        try:
            self.client.getpeername()
            return True
        except Exception as e:
            return False
        finally:
            pass
    def GetServerInfo(self):
        try:
           result= self.client.getpeername()
           return result
        except Exception as e:
            return ('127.0.0.1',000)
        finally:
            pass 
    def CloseConnect(self):
        try:
            self.client.close()
            return True
        except Exception as e:
            return False
        finally:
            pass
        
 
