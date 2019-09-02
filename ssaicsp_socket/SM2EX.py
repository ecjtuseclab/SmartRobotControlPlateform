# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""


import SM3
import SM2
class SM2EX:
    len_para=0#参数长度
    def __init__(self,pubkey="",prikey=""):# 构造函数
        self.PublicKey=pubkey
        self.PrivateKey=prikey
        self.len_para=int(SM2.Fp/4)
        if len(self.PublicKey)==0 or len(self.PrivateKey)==0:#公钥私钥未赋值时自动生成秘钥对
            self.GenSM2KeyPair()
        pass
    def GenSM2KeyPair(self,hashvlue=""):#生成秘钥对，可根据 Hash值生成或随机生成
        if hashvlue!="" and len(hashvlue)==64:#根据Hash值生成秘钥对
            self.PrivateKey=hashvlue
        else:#随机生成秘钥对
            self.PrivateKey=SM2.get_random_str(self.len_para)
        self.PublicKey=SM2.kG(int(self.PrivateKey,16),SM2.sm2_G,self.len_para)
        return self.PrivateKey,self.PublicKey#返回 私钥，公钥
    def SM2Sign(self,msg,prikeyHex=""):#签名生成
        if prikeyHex!="":
            self.PrivateKey=prikeyHex
        hashMsg=SM3.Hash_sm3(msg)
        k=SM2.get_random_str(self.len_para)
        sign=SM2.Sign(hashMsg,self.PrivateKey,k,self.len_para,1)
        return sign
    def SM2Verify(self,msg,sign,pubkey=""):#签名验证
        if pubkey!="":
            self.PublicKey=pubkey
        hashMsg=SM3.Hash_sm3(msg)
        result=SM2.Verify(sign,hashMsg,self.PublicKey,self.len_para)
        return result
    def SM2Encrypt(self,msg,pubkey=""):#明文加密
        if pubkey!="":
            self.PublicKey=pubkey
        cipher=SM2.Encrypt(msg,self.PublicKey,self.len_para,0)
        return cipher
    def SM2Decrypt(self,cipher,prikey=""):#明文解密
        if prikey!="":
            self.PrivateKey=prikey
        plainHex=SM2.Decrypt(cipher,self.PrivateKey,self.len_para) 
        plain=str(bytes.fromhex(plainHex))
        return plain[2:len(plain)-1]
    def SM3Hash(self,msg):
        hashHex=SM3.Hash_sm3(msg)
        return hashHex
'''
pubkey='2423B4B96630B779C12679F1D9C40295CD11029DB2FB288ADB697C96C58C5E5B01A1EEE6867288381727A1665CFE568ACD65AAF4F43AFD6FA10D51748BC934DE'
prikey='406E61F829642037D72ECC4C431DD47A4D4DC374FB7DE408DCFCF73C81ADE78C'
sm2=SM2EX(pubkey,prikey)
mesage="12345678"
sign="3C1A3C0339774B3AA695DA6983B7D202F805299369CB0E649A66CA5A58812C748CFED8EA57B25B58BFE60214B9FCF25ED8D145EAA7A1F95B9559CF2BB9906F49"
print(sm2.SM2Verify(mesage,sign))
cipher="3F7351427B17DB8C15F9360596B3AD891CAEF82FD3C5CFC1D9A9223A59801CF05F1399E532B284F7C7D52FB8F3B20259858B7EC3A5CF394CBD769C97054F282D3C885754A7F72ED32A8C671D1B6E6C9382E0101B05BDE3756B46278590E4B4DC229F0A501ABF116E"
print(cipher)
plain=sm2.SM2Decrypt(cipher)
print(plain)
        

print(">>"*10,"使用示例","<<"*10)
sm2=SM2EX()
print("**"*10,"秘钥生成：","**"*10)
prikey,pubkey=sm2.GenSM2KeyPair()

print("privatekey:",prikey)
print("publickey:",pubkey)
print("**"*10,"签名生成与验证：","**"*10)
msg="12345678"
print("message:",msg)
sign=sm2.SM2Sign(msg)
print("signResult:",sign) 
print("VerifyResult:",sm2.SM2Verify(msg,sign))
print("**"*10,"加密与解密：","**"*10)
cipher=sm2.SM2Encrypt(msg)
print(msg,">对应密文>:",cipher)
plain=sm2.SM2Decrypt(cipher)
print("解密结果：",plain)

print("--"*10,"根据给定秘钥对执行","--"*10)
pubkey='2423B4B96630B779C12679F1D9C40295CD11029DB2FB288ADB697C96C58C5E5B01A1EEE6867288381727A1665CFE568ACD65AAF4F43AFD6FA10D51748BC934DE'
prikey='406E61F829642037D72ECC4C431DD47A4D4DC374FB7DE408DCFCF73C81ADE78C'
print("**"*10,"给定秘钥对","**"*10)
print("privatekey:",prikey)
print("publickey:",pubkey)
print("**"*10,"签名生成与验证：","**"*10)
msg="12345678"
print("message:",msg)
sign=sm2.SM2Sign(msg,prikey)
print("signResult:",sign) 
print("VerifyResult:",sm2.SM2Verify(msg,sign,pubkey))
print("**"*10,"加密与解密：","**"*10)
cipher=sm2.SM2Encrypt(msg,pubkey)
print(msg,">对应密文>:",cipher)
plain=sm2.SM2Decrypt(cipher,prikey)
print("解密结果：",plain)


print("XX"*6,"根据给定信息Hash后的值生成密钥对","XX"*6)
info="czs1993"
print("给定信息：",info)
hashinfo=SM3.Hash_sm3(info)
print("SM3处理后Hash值：",hashinfo)
prikey,pubkey=sm2.GenSM2KeyPair(hashinfo)
print("**"*10,"根据Hash生成的钥对","**"*10)
print("privatekey:",prikey)
print("publickey:",pubkey)
print("**"*10,"签名生成与验证：","**"*10)
msg="12345678"
print("message:",msg)
sign=sm2.SM2Sign(msg)
print("signResult:",sign) 
print("VerifyResult:",sm2.SM2Verify(msg,sign))
print("**"*10,"加密与解密：","**"*10)
cipher=sm2.SM2Encrypt(msg)
print(msg,">对应密文>:",cipher)
plain=sm2.SM2Decrypt(cipher)
print("解密结果：",plain)
'''
            
