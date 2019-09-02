# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from threading import Timer 
from BasePacket import *
from SensorPacket import *
from InformPacket import *
from DataProtocol import *
from SocketClient import * 
from MessageControlCenter import *
import threading
import random
from activebuzzer import *
from ultrasonic import *
from light import *
from fire import *
from soil import *
from rain import *
from dht11 import *
from smoke import *
from led import *
from OperateMysql import *
from KeyAgreementProcessProtocol import *
import AESHelper 
from  SM2EX import *
from Logger import *

class MainPanel: 
##Confing Infos    
    RPiID = '' #树莓派编号
    RPINAME = '' #树莓派别名
    
    Remote_ServerHost = ''
    #Host=''#服务器IP
    Remote_ServerPort = 8666
    #Port=8666#服务器端口
    
    Local_ServerHost = '127.0.0.1'
    #LocalServerHost=''	#树莓派ip
    Local_ServerPort = 8888
    #SPort=8888
    
    Local_ServerMaxConCount = 10
    #MaxConnectCount=10#连接池最大数
    Local_ClientCount = 10
    #ClientCount=10
    
    SendTime_interval=10#数据发送间隔时间  sendtime
    CheckConTime_interval=30#连接池连接状态检测 checkcontime
    
    Clients = []
    SensorsObjectDic = {}#传感器集合
    CurrentState = 'stop'
    
    #设备SM2密钥对
    Pubkey='2423B4B96630B779C12679F1D9C40295CD11029DB2FB288ADB697C96C58C5E5B01A1EEE6867288381727A1665CFE568ACD65AAF4F43AFD6FA10D51748BC934DE'
    Prikey='406E61F829642037D72ECC4C431DD47A4D4DC374FB7DE408DCFCF73C81ADE78C'
    
    Sensors={1:'activebuzzer',2:'aroadtracing',3:'dht11',4:'fire',
    5:'human',6:'infraredemission',7:'infraredreception',8:'light',
    9:'obstacleavoidance',10:'rain',11:'smoke',12:'soil',
    13:'sound',14:'ultrasonic',15:'led'}
    
    def __init__(self):
        #设置日志
        self.log = Logger('logging.log',logging.ERROR,logging.DEBUG)
        self.SendCount=0
        try:       
            self.sm2=SM2EX(self.Pubkey,self.Prikey)
            self.mysql = OperateMysql()
            self.sendTimer=Timer(self.SendTime_interval,self.SendSensorData)
            self.connectStateTimer=Timer(self.CheckConTime_interval,self.CheckConnectState)         
            
            #设置设备信息
            equipment = self.mysql.GetData("select rpi_code,rpi_name,remote_serverhost,remote_serverport,local_serverhost,local_serverport,local_servermaxconcount,local_clientcount,sendtime,checkcontime,equipmentkey,isciphertransfer from ssaicsp_equipments")
            print(equipment)
            self.log.debug('设备信息为：'+str(equipment))
            self.RPiID = equipment[0][0]
            self.RPINAME = equipment[0][1]
            self.Remote_ServerHost = equipment[0][2]
            self.Remote_ServerPort = equipment[0][3]
            self.Local_ServerHost = equipment[0][4]
            self.Local_ServerPort = equipment[0][5]
            self.Local_ServerMaxConCount = equipment[0][6]
            self.Local_ClientCount = equipment[0][7]
            self.SendTime_interval = equipment[0][8]
            self.CheckConTime_interval = equipment[0][9]
            self.EquipmentKey=equipment[0][10] 
            self.IsCipherTransfer=equipment[0][11] #增加是否加密传输
            pass
        except Exception as e: 
            self.log.error('初始化设备失败，错误为：'+str(e))
    
    #命令方法#后续补充
    def Shell(self):
        while True:
              cmd=input("EnterCommand:")
              if cmd=='start':
                  self.CurrentState=cmd 
                  #初始化传感器
                  self.InitSeneorsDic() 
                  #开启server服务
                  self.ServerInit()
                  self.StartServer()   
                  #开启client服务
                  #self.StartClient()
              elif cmd=='send':
                  self.StartSendTimer()
              elif cmd=='stop':
                  self.CurrentState=cmd
                  self.socketClient.CloseConnect()
              elif cmd=='quit': 
                  break
        pass
    #添加传感器
    def InitSeneorsDic(self):
        try:
            self.SensorsObjectDic.clear()
            # ControlData = str(enable)+','+str(acqfre)+','+str(rediscount)+','+str(parameters)
            # Data = '2*'+str(type)+'*'+str(sensor_code)+'*'+str(pins)+'*'+ControlData
            sensors = self.mysql.GetData("select type,sensor_code,pins,enable,acqfre,rediscount,parameters,tranfre,keep_time from ssaicsp_sensors")       
            for sensor in sensors:
                controldata = str(sensor[3])+','+str(sensor[4])+','+str(sensor[5])+','+str(sensor[6])
                sensortype = int(sensor[0])
                #print(sensortype,controldata)
                self.log.debug('传感器：sensortype='+str(sensortype)+',controldata='+controldata)
                
                if sensortype == 1:
                    #添加蜂鸣传感器
                    act = activebuzzer(sensor[0],sensor[1],sensor[2],controldata)
                    act.Start()
                    self.SensorsObjectDic[act.GetKey()] = act  
                    self.log.debug('添加传感器'+act.GetKey())
               
                elif sensortype == 2:
                    self.log.debug('添加传感器'+str(sensortype))
       
                elif sensortype == 3:
                    #添加一个温湿度传感器
                    dht = dht11(sensor[0],sensor[1],sensor[2],controldata)
                    dht.Start()
                    self.SensorsObjectDic[dht.GetKey()] = dht  
                    self.log.debug('添加传感器'+dht.GetKey())
                elif sensortype == 4:
                    #添加一个火焰传感器
                    fir = fire(sensor[0],sensor[1],sensor[2],controldata)
                    fir.Start()
                    self.SensorsObjectDic[fir.GetKey()] = fir    
                    self.log.debug('添加传感器'+fir.GetKey())
                                          
                elif sensortype == 5:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 6:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 7:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 8:
                    #添加一个光敏传感器
                    lig = light(sensor[0],sensor[1],sensor[2],controldata)
                    lig.Start()
                    self.SensorsObjectDic[lig.GetKey()] = lig 
                    self.log.debug('添加传感器'+lig.GetKey())
                                          
                elif sensortype == 9:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 10:
                    #添加一个雨滴传感器
                    ran = rain(sensor[0],sensor[1],sensor[2],controldata)
                    ran.Start()
                    self.SensorsObjectDic[ran.GetKey()] = ran 
                    self.log.debug('添加传感器'+ran.GetKey())
                                          
                elif sensortype == 11:
                    #添加一个烟雾传感器
                    smk = smoke(sensor[0],sensor[1],sensor[2],controldata)
                    smk.Start()
                    self.SensorsObjectDic[smk.GetKey()] = smk  
                    self.log.debug('添加传感器'+smk.GetKey())
                                          
                elif sensortype == 12:
                    #添加一个土壤传感器
                    sol = soil(sensor[0],sensor[1],sensor[2],controldata)
                    sol.Start()
                    self.SensorsObjectDic[sol.GetKey()] = sol 
                    self.log.debug('添加传感器'+sol.GetKey())
                                          
                elif sensortype == 13:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 14:
                    #添加一个测距传感器
                    ult = ultrasonic(sensor[0],sensor[1],sensor[2],controldata)
                    ult.Start()
                    self.SensorsObjectDic[ult.GetKey()] = ult 
                    self.log.debug('添加传感器'+ult.GetKey())
    
                elif sensortype == 15:
                    #添加led
                    l1d = led(sensor[0],sensor[1],sensor[2],controldata)
                    l1d.Start()
                    self.SensorsObjectDic[l1d.GetKey()] = l1d  
                    self.log.debug('添加传感器'+l1d.GetKey())
    
                elif sensortype == 16:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 17:
                    self.log.debug('添加传感器'+str(sensortype))
                elif sensortype == 18:
                    self.log.debug('添加传感器'+str(sensortype))
                else:
                    #print('添加传感器',sensortype , '错误')
                    self.log.debug('添加传感器'+str(sensortype) +'错误')
            pass
        except Exception as e: 
            self.log.error('初始化设备失败，错误为：'+str(e))
    
    #开启SOCKETServer
    def ServerInit(self):
        try:
            self.SocketServer=socket.socket()
            self.SocketServer.bind((self.Local_ServerHost,self.Local_ServerPort))
            self.SocketServer.listen(self.Local_ServerMaxConCount)
            pass
        except Exception as e: 
            self.log.error('ServerInit()失败，错误为：'+str(e))
    
    def StartServer(self):
        try:
            thread=threading.Thread(target=self.Server_handle)
            thread.start()
            pass
        except Exception as e: 
            self.log.error('StartServer()失败，错误为：'+str(e))
    
    #开启异步监听（树莓派自身web发送封包到树莓派中）
    def Server_handle(self):
        try:
            while True:    
                conn,address=self.SocketServer.accept()
                while True:
                     try:
                         #接受到的控制命令
                         data=conn.recv(1024)
                         if not data:break
                         #处理封包
                         outpacket = self.PacketProcess(data)
                         if outpacket.DataLength > 0:
                             #print('返回树莓派web封包数据为：',outpacket.PacketStr)
                             self.log.debug('返回树莓派web封包数据为：'+outpacket.PacketStr)
                             conn.sendall(str(outpacket.PacketStr).encode('utf-8'))
                         #返回结果
                     except Exception as e:
                         break
            pass
        except Exception as e: 
            self.log.error('Server_handle()失败，错误为：'+str(e))
    
    #接收信息回调函数（数据中心发送封包到树莓派中）
    def Receive(self,message):#接收信息后更新
        try:
            outpacket = self.PacketProcess(message) 
            if   outpacket.DataLength> 0:       
               #print('返回数据中心封包数据为：',outpacket.PacketStr)
               self.log.debug('返回数据中心封包数据为：'+outpacket.PacketStr)
               self.SendMessage(outpacket.PacketStr)
            pass
        except Exception as e: 
            self.log.error('Receive()失败，错误为：'+str(e))
        
    #响应控制命令
    def PacketProcess(self,message):
        try:
            self.log.debug('PacketProcess,'+str(message))
            
            outpacket=BasePacket()    #响应封包
            packet=BasePacket()       #接收封包
            flag = False
            
            if packet.IsPacket(message):
               packet.StrToPacket(message)
               #print('一级封包类型', packet.PacketType)
               self.log.debug('一级封包类型'+str(packet.PacketType))
    		  
               #组装返回封包
               outpacket.StartNode = packet.EndNode
               outpacket.EndNode = packet.StartNode
                 
               if(packet.PacketType==1):
                   kaa=KeyAgreementProcessProtocol()
                   kaa.SN=self.RPiID 
                   outpacket=kaa.AnalyzePacket(packet)
                   ##从数据库中获取一下设备 密钥
                   key_data=self.mysql.GetData("SELECT equipmentkey from ssaicsp_equipments WHERE  rpi_code="+self.RPiID)
                   self.EquipmentKey=key_data[0][0] 
                   #print("Key:",self.EquipmentKey)
                   self.log.debug("Key:"+str(self.EquipmentKey))
               elif(packet.PacketType==11):    #注册封包
                   outpacket.PacketType=1
                   outpacket.Data=""#packet.Data+"_Execute Successful!"
                   outpacket.DataLength=len(outpacket.Data) 
                   self.log.debug('11packet')
               
               elif packet.PacketType == 21:   #设备通知封包
                   #print(packet.GetPacketType())
                   for temp in self.SensorsObjectDic:
                       #print('重启设备', temp)
                       self.log.debug('重启设备')
                       self.SensorsObjectDic[temp].Stop()   
                   self.InitSeneorsDic()
                   
               elif packet.PacketType == 22:  #传感器通知封包
                    #print('22packet')
                    self.log.debug('22packet')
                    
               elif packet.PacketType == 31:  #设备控制封包
                    #print('31packet')
                    self.log.debug('31packet')
                    
               elif packet.PacketType == 32:  #传感器控制封包   
                    #定义个用于处理传感器控制的封包             
                    spacket = SensorPacket()
                    spacket.StrToPacket(packet.Data)
                    temp = self.SensorsObjectDic[spacket.GetKey()]
                    flag = temp.SensorController(spacket)
                    
                    ioutpacket = InformPacket()
                    ioutpacket.ControlName = spacket.ControlName
                    ioutpacket.SensorType = spacket.SensorType
                    ioutpacket.SensorCode = spacket.SensorCode
                    if flag == True:
                        ioutpacket.ControlStatus = 'success'
                        ioutpacket.ControlMsg = 'control success!'
                    else:
                        ioutpacket.ControlStatus = 'fail'
                        ioutpacket.ControlMsg = 'control fail!'
                
                    ioutpacket.PacketToStr()
                    outpacket.PacketType = '22'
                    outpacket.Data = ioutpacket.PacketStr                
               else:
                   #print('未知封包！', message)
                   self.log.debug('未知封包！'+ str(message))
               
               
               outpacket.SignInfo=self.sm2.SM2Sign(outpacket.Data)
               outpacket.PacketToStr()
            return outpacket
        except Exception as e: 
            self.log.error('PacketProcess()失败，错误为：'+str(e))
     
    #维持连接池方法上
    def CheckConnectState(self):
        try:
            count=len(self.Clients)
            end=(count if count<=self.Local_ClientCount else self.Local_ClientCount) 
            for i in range(0,end):#检查Clientts集合中连接状态
                temp=self.Clients[i]
                if temp.IsConnected()==False:
                    self.Clients.pop(i)
                    client=SocketClient(self.Remote_ServerHost,self.Remote_ServerPort,self)
                    client.ConnectServer()
                    self.Clients.append(client)
            for j in range(count,self.Local_ClientCount):#补充连接集合
                client=SocketClient(self.Remote_ServerHost,self.Remote_ServerPort,self)
                client.ConnectServer()
                self.Clients.append(client) 
            pass
        except Exception as e: 
            self.log.error('CheckConnectState()失败，错误为：'+str(e))
    #SOCKETClient事件。。。。。。。。。。。。。。。。。。。。。。。。。
    #客户端停止 
     #开启客户端 
    def StartClient(self):
        try:
            #开启十个Client连接
            for i in range(0,self.Local_ClientCount):
                temp=SocketClient(self.Remote_ServerHost,self.Remote_ServerPort,self)
                temp.ConnectServer()  
                self.Clients.append(temp)
            self.Register()
            self.KeyAgreement()#开启密钥协商
            return True
            pass
        except Exception as e: 
            self.log.error('StartClient()失败，错误为：'+str(e))
    
    def ClientStop(self):
        try:
            self.socketClient.CloseConnect()
            self.sendTimer.cancel()
            self.sendTimer=Timer(self.SendTime_interval,self.SendSensorData)
            pass
        except Exception as e: 
            self.log.error('ClientStop()失败，错误为：'+str(e))

    def KeyAgreement(self):
        try:
            kapp=KeyAgreementProcessProtocol()
            kapp.SN=self.RPiID
            packet=kapp.KeyAgreementStep0()
            if(packet.DataLength>0):
                self.SendMessage(packet.PacketToStr())
            pass
        except Exception as e: 
            self.log.error('KeyAgreement()失败，错误为：'+str(e))
          
    def Register(self):
        try:
            packet=BasePacket()
            packet.StartNode=self.RPiID
            packet.EndNode="11111"
            packet.PacketType=11
            packet.Data=self.RPiID+"*"+self.Local_ServerHost
            packet.DataLength=len(packet.Data)
            self.SendMessage(packet.PacketToStr())
        except Exception as e: 
            self.log.error('Register()失败，错误为：'+str(e))
    
    #开启发送定时器
    def StartSendTimer(self):
        try:
            #如果开启了定时发送数据
            if self.SendTime_interval > 0 :
                self.sendTimer.start()
            pass
        except Exception as e: 
            self.log.error('StartSendTimer()失败，错误为：'+str(e))
    
    #发送传感器数据方法（非实时）
    def SendSensorData(self):
        try:
            #如果开启的定时发送数据
            if self.SendTime_interval > 0:
                self.sendTimer=Timer(self.SendTime_interval,self.SendSensorData)
                self.sendTimer.start()
                dp = DataProtocol()
                packet = BasePacket()
                #tempRedis=Redis(host='127.0.0.1',port=6379)
                #key=tempRedis.get('Equipmetkey')#读取密钥
                for i in range(1,16):#根据传感器发送数据
                    sensordata = dp.GetDataPacket(i) ##代表温度传感器 
                    packet.StartNode = self.RPiID
                    packet.EndNode = '11111'
                    packet.PacketType = 41
                    if int(self.IsCipherTransfer)==1:
                        sensordata=AESHelper.Encrypt(sensordata,self.EquipmentKey) # sensordata 加密传输数据
                    packet.Data = sensordata
                    packet.PacketToStr()
                    
                    if packet.DataLength>0:
                        #print(packet.PacketStr)
                        self.SendMessage(packet.PacketStr)  
            pass 
        
            '''
            #从数据库中读出传感器数据发送至数据中心
            self.sendTimer=Timer(self.SendTime_interval,self.SendSensorData)
            self.sendTimer.start()
            dp=DataProtocol()
            for i in range(1,17):#根据传感器发送数据
                packet=dp.GetDataPacket(i)##代表温度传感器
                packet.RPiID=MPanel.RPiID 
                packet.PacketToStr()
                if packet.DataLen>0:
                    self.SendMessage(packet.PacketStr)  
            pass 
            '''
        except Exception as e: 
            self.log.error('SendSensorData()失败，错误为：'+str(e))
    
    #发送信息
    def SendMessage(self,message):#信息发送方法
        try:
            clientcount=len(self.Clients);
            if clientcount>0:
                index=self.SendCount%clientcount
                self.SendCount=self.SendCount+1 
                if self.SendCount>10000000:
                    self.SendCount=0 #清空发送计数，防止整数溢出
                client=self.Clients[index]
                client.SendMessage(message)
            else:
                #记录到发送失败日志
                self.log.war(str(message)+'发送失败！')
                pass
            pass
        except Exception as e: 
            self.log.error('SendMessage()失败，错误为：'+str(e))
  
MPanel=MainPanel()
MPanel.Shell()
