# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

import logging,os

class Logger:
    def __init__(self, path,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        self.logger = logging.getLogger('log/'+path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        #设置文件日志
        fh = logging.FileHandler('log/'+path)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def war(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def cri(self,message):
        self.logger.critical(message)
'''
if __name__ =='__main__':
    logyyx = Logger('logging.log',logging.ERROR,logging.DEBUG)
    logyyx.debug('一个debug信息'+'ssss')
    logyyx.info('一个info信息')
    logyyx.war('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri(str('一个致命critical信息'+'kk'))
'''