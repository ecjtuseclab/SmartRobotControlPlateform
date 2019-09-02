# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from BasePacket import *
from DataProtocol import *

class MessageControlCenter():
    protocols = {1:DataProtocol()}
    packet = BasePacket()
    def __init__(self):
        pass
    def PacketMachine(self,inpacket):
        packet=inpacket 
        if packet.PacketType==1: 
            dp=DataProtocol()
            dp.UpdateStatus(packet)
        
