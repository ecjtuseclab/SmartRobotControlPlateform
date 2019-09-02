# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from Crypto.Cipher import AES  
def ByteToHex(bins ): 
    return ''.join( [ "%02X" % x for x in bins ] ).strip()

def Encrypt(msg,key): 
    msglen=len(msg) 
    standlen=16 
    add=standlen-(msglen%standlen)
    addstr=""
    iv=key#"1234567887654321"
    if add!=16: 
        addstr="*"+"0"*(add-1)
    aes=AES.new(key, AES.MODE_CBC, iv)
    cipher=aes.encrypt(msg+addstr) 
    return ByteToHex(cipher)
def Decrypt(cipher,key):
    iv=key#"1234567887654321"
    aes= AES.new(key, AES.MODE_CBC, iv)
    plain=aes.decrypt(bytes.fromhex(cipher))
    return plain  