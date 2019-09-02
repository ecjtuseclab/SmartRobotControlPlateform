# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from OperateMysql import *
class EquipmentInfos():
    def __init__(self,sn):
        self.mysql=OperateMysql()
        data=self.mysql.GetData("SELECT equipmentInfos from ssaicsp_equipments  where  rpi_code="+sn)
        self.EquipemtnInfoStr=data[0][0]
        InfoList=self.EquipemtnInfoStr.split('*')
        self.SN=sn
        self.Ver=InfoList[0]
        self.Type=1
        self.Subtype=1
        self.Len=0 
        self.SIM=InfoList[1]
        self.EquipmentID=InfoList[2]
        self.Cert=InfoList[3]
    def Step1HashPlain(self):
        self.Len=len(str(self.Type)+str(self.Subtype)+self.Ver+self.SN+self.SIM+self.EquipmentID)
        return (str(self.Type)+str(self.Subtype)+str(self.Len)+self.Ver+self.SN+self.SIM+self.EquipmentID+self.Cert)
        pass
    def Step2HashPlain(self):
        self.Len=len(str(self.Type)+str(self.Subtype+1)+self.SN+"1")
        return (str(self.Type)+str(self.Subtype+1)+str(self.Len)+self.SN+"1")
       
