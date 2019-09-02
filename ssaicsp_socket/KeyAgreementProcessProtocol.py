# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from EquipmentInfos import *
from OperateMysql import *
from  SM2EX import *
from BasePacket import *
import random
class KeyAgreementProcessProtocol():
    Pubkey='2423B4B96630B779C12679F1D9C40295CD11029DB2FB288ADB697C96C58C5E5B01A1EEE6867288381727A1665CFE568ACD65AAF4F43AFD6FA10D51748BC934DE'
    Prikey='406E61F829642037D72ECC4C431DD47A4D4DC374FB7DE408DCFCF73C81ADE78C'
    def __init__(self):
        self.sm2=SM2EX(self.Pubkey,self.Prikey)
        self.CurrentStep=0;
        self.mysql=OperateMysql()
        self.SN=""
        self.DataList=[]
        pass
    def AnalyzePacket(self,packet): 
        self.DataList=packet.Data.split('*')
        snstr=self.DataList[0]
        print(snstr)
        self.SN=snstr[0:5]
        if(len(snstr)==6):
            self.CurrentStep=int(snstr[5:6])
        if self.CurrentStep==0:
           packet=self.KeyAgreementStep0()
        elif self.CurrentStep==1:
           packet=self.KeyAgreementStep1(packet) 
        return packet 
            
    def KeyAgreementStep0(self):
        #随机数
        packet=BasePacket()
        packet.StartNode=self.SN
        packet.PacketType=1
        packet.EndNode=""
        R1=self.GetRandomIntStr(8)
        equipmentinfo=EquipmentInfos(self.SN)
        Ecert=self.sm2.SM2Encrypt(R1) #self.sm2.SM2Encrypt(R1)
        hvalue=equipmentinfo.Step1HashPlain()+Ecert
        Eskey=self.sm2.SM2Sign(hvalue)
        packet.Data=self.SN+"*"+Ecert+"*"+Eskey 
        packet.DataLength=len(packet.Data)
        self.mysql.SaveData("Update ssaicsp_equipments set r1="+R1+"  where rpi_code="+self.SN)
        return packet 
    def KeyAgreementStep1(self,packet):  
        equipmentinfo=EquipmentInfos(self.SN)
        R2=self.sm2.SM2Decrypt(self.DataList[1])  
        data=self.SN+"2*"
        #验证签名  
        hvalue=equipmentinfo.Step2HashPlain()+self.DataList[1]
        vresult=self.sm2.SM2Verify(hvalue,self.DataList[2]) 
        hr1_r2=""  
        if(vresult):#验证通过
            r1_data=self.mysql.GetData("SELECT r1 from ssaicsp_equipments WHERE  rpi_code="+self.SN)
            R1=r1_data[0][0]
            r1_r2hex=self.GetHR1_R2Hex(R1,R2) 
            hr1_r2=self.sm2.SM3Hash(str(r1_r2hex))  
            data=data+hr1_r2
        packet.Data=data
        print("OK")  	
        self.mysql.SaveData("Update ssaicsp_equipments  set r2="+R2+" ,equipmentkey='"+r1_r2hex+"'   where rpi_code="+self.SN)
        return packet
        pass
    def KeyAgreementStep2(self,packet):
        pass
    def GetHR1_R2Hex(self,r1,r2):
        r1_r2byte=[]
        r1byte=bytes(str(r1),'utf-8')
        r2byte=bytes(str(r2),'utf-8')
        for index in range(0,len(r1byte)):
            r1_r2byte.append(r1byte[index]^r2byte[index])
        return self.ByteToHex(r1_r2byte)
    def ByteToHex(self, bins ): 
         return ''.join( [ "%02X" % x for x in bins ] ).strip()

    def GetRandomIntStr(self,strlen):
        random_str=""
        base_str="1234567890"
        length=len(base_str)-1
        for i in range(strlen):
            random_str+=base_str[random.randint(0,length)]
        return random_str
        
