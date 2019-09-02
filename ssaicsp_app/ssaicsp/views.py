# -*- coding:UTF-8 -*-
"""
Created on Mon Jul  9 20:41:03 2018

@author: 康文洋 kangwenyangde@163.com、陈祚松、夏萍萍、艾美珍、陈兰兰、张梦丽、易传佳
"""

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
#from django.core import serializers
from django.forms.models import model_to_dict
from datetime import date,datetime
import json
from ssaicsp import models
import math
import operator
from django.views.decorators.csrf import csrf_exempt
import socket
#from SocketClient import *

# Create your views here.
#获得设备的信息
def getequipments(request):
    queryset = models.equipments.objects.all()
    records = models.equipments.objects.count()
    print('getequipments')
    json_data = backjson(1,records,records,queryset)
    return HttpResponse(json_data)

#获得传感器的信息
def getsensors(request):
    queryset = models.sensors.objects.all().order_by('sensor_code')
    records = models.sensors.objects.count()
    json_data = backjson(1,records,records,queryset)
    return HttpResponse(json_data)

#重启设备
def restartequipments(request):
    queryset = models.equipments.objects.all()
    #cmdmsg封包格式：树莓派编号#封包类型#传感器类型#传感器编号#传输数据内容#数据长度#数字签名
    #传输数据内容（采集频率、引脚）
    cmd = "4"
    cmdmsg = str(queryset[0].rpi_code)+'#1#2#3#'+cmd+'#'+str(len(cmd))+'#xxx'
    #此处socket需要放入try中
    SendMsgToServer(cmdmsg)
    #此处应该根据返回值做判断
    json_data = backajax('success','重启设备成功！')
    return HttpResponse(json_data)
	
#编辑设备信息
@csrf_exempt
def editequipments(request):
	
	tbid = request.POST['id']
	rpi_code = request.POST['rpi_code']
	rpi_name = request.POST['rpi_name']
	remote_serverhost = request.POST['remote_serverhost']
	remote_serverport = request.POST['remote_serverport']
	local_serverhost = request.POST['local_serverhost']
	local_serverport = request.POST['local_serverport']
	local_servermaxconcount = request.POST['local_servermaxconcount']
	local_clientcount = request.POST['local_clientcount']
	sendtime = request.POST['sendtime']
	checkcontime = request.POST['checkcontime']
	remark = request.POST['remark']

	#根据id从数据库读出数据
	equipments = models.equipments.objects.get(id = tbid)
	#将新配置存入数据库中
	equipments.rpi_code = rpi_code
	equipments.rpi_name = rpi_name
	equipments.remote_serverhost = remote_serverhost
	equipments.remote_serverport = remote_serverport
	equipments.local_serverhost = local_serverhost
	equipments.local_serverport = local_serverport
	equipments.local_servermaxconcount = local_servermaxconcount
	equipments.local_clientcount = local_clientcount
	equipments.sendtime = sendtime
	equipments.checkcontime = checkcontime
	equipments.create_time = datetime.now()
	equipments.remark = remark

	equipments.save()

	return HttpResponse(str('kkkkk'))

#编辑传感器信息
@csrf_exempt
def editsensors(request):
    #12120行 POST数据形式为acqfre:''  tranfre:'' 只有可编辑的字段才会以POST 的形式将字段数据post到后端
    tbid = request.POST['id']
    #rpicode = request.POST['sensor_code']
    sensor_code = request.POST['sensor_code']
    sensor_name = request.POST['sensor_name']
    type = request.POST['type'] 
    acqfre = request.POST['acqfre']
    tranfre = request.POST['tranfre']
    enable = request.POST['enable']
    keep_time = request.POST['keep_time']   
    rediscount = request.POST['rediscount']
    pins = request.POST['pins']
    parameters = request.POST['parameters']
    #create_time = request.POST['create_time']
    remark = request.POST['remark']
    
    #设备级别的控制
    #  StartNode#EndNode#PacketType#Data#DataLength#Sign    
    #  Data = ControlName*SensorType*SensorCode*SensorPins*ControlData
    #  ControlData = 是否启用、采集频率、数据缓存条数
    
    ControlData = str(enable)+','+str(acqfre)+','+str(rediscount)+','+str(parameters)
    Data = '2*'+str(type)+'*'+str(sensor_code)+'*'+str(pins)+'*'+ControlData
    #获取节点信息
    node = models.equipments.objects.all()[:1]
    PacketData = str(node[0].rpi_code) + '#' + str(node[0].rpi_code) + '#32#' + Data
    cmdmsg = PacketData+'#'+str(len(PacketData))+'#sign'
    #print(cmdmsg)
    
    #将修改的信息发送给Server端
    SendMsgToServer(cmdmsg)
    
    #根据id从数据库读出数据
    sensor = models.sensors.objects.get(id = tbid)
    #将新配置存入数据库中
    sensor.sensor_code = sensor_code
    sensor.sensor_name = sensor_name
    sensor.type = type
    sensor.acqfre = acqfre
    sensor.tranfre = tranfre
    sensor.enable = enable
    sensor.keep_time = keep_time
    sensor.rediscount = rediscount
    sensor.pins = pins
    sensor.parameters = parameters
    sensor.create_time = datetime.now()
    sensor.remark = remark
    sensor.save()
    
    #return HttpResponseServerError("ssssssssssssss")
    return HttpResponse(str(type))
    
#编辑传感器控制命令信息
@csrf_exempt
def controlsensor(request):
    #12120行 POST数据形式为acqfre:''  tranfre:'' 只有可编辑的字段才会以POST 的形式将字段数据post到后端
    controlname = request.POST['controlname']
    type = request.POST['type']
    sensor_code = request.POST['sensor_code']
    parameters = request.POST['parameters'] 
    pins = ""
    
    #设备级别的控制
    #  StartNode#EndNode#PacketType#Data#DataLength#Sign    
    #  Data = ControlName*SensorType*SensorCode*SensorPins*ControlData
    #  ControlData = 是否启用、采集频率、数据缓存条数
    
    ControlData = str(parameters)
    Data = str(controlname)+'*'+str(type)+'*'+str(sensor_code)+'*'+str(pins)+'*'+ControlData
    #获取节点信息
    node = models.equipments.objects.all()[:1]
    #PacketData = str(node[0].rpi_code) + '#' + str(node[0].rpi_code) + '#32#' + Data
    PacketData = '12345#' + str(node[0].rpi_code) + '#32#' + Data
    cmdmsg = PacketData+'#'+str(len(PacketData))+'#sign'
    print(cmdmsg)
    
    #将修改的信息发送给Server端
    SendMsgToServer(cmdmsg)
    
    #根据sensor_code从数据库读出数据
    sensor = models.sensors.objects.get(sensor_code = sensor_code)
    if controlname == '12':
        sensor.parameters = parameters
    sensor.save()
    print(sensor_code,'保存成功！')
    
    #return HttpResponseServerError("ssssssssssssss")
    return HttpResponse(str(type))
    
#向服务器发送传感器信息，重置传感器
def SendMsgToServer(cmdmsg):
	try:
		#创建SocketClient
		host = '127.0.0.1'
		port = 8888
		#cmdmsg封包格式：树莓派编号#封包类型#传感器类型#传感器编号#传输数据内容#数据长度#数字签名
		#传输数据内容（采集频率、引脚）
		#cmd = "4"
		#cmdmsg = str(queryset[0].rpi_code)+'#1#2#3#'+cmd+'#'+str(len(cmd))+'#xxx'
		'''
		client = SocketClient(host, port)
		client.ConnectServer()
		if client.IsConnected():
			client.SendMessage(cmdmsg)
			result = client.Receive()
		'''
		s = socket.socket();
		s.connect((host, port))
		s.send(cmdmsg.encode('UTF-8'))
		print("send cmdmsg:"+cmdmsg)

		result = s.recv(1024)
		s.close()
		print("result:"+str(result))
		
		return Ture
	except Exception as e:
		return False
	
	return str(result)


def index(request):
	menu_dict = {1: {'name': '一类传感器', 'nav': {
										'ultrasonic': '超声波', 'smoke': '烟雾', 'fire': '火焰', 'light': '光敏', 'soil': '土壤', 'rain': '雨滴', 'current':'电流'}},
								2: {'name': '二类传感器', 'nav': {
										'dht11': '温湿度',  'sound': '声音', 'obstacleavoidance': '避障', 'aroadtracing': '寻迹', 'infraredemission': '红外发射', 'infraredreception': '红外接受'}},
								3: {'name': '三类传感器', 'nav': {'human': '人体'}},
								4: {'name': '四类传感器', 'nav': {'led': 'led', 'relay':'继电器', 'activebuzzer': '蜂鸣器'}},								
								5: {'name': '设置', 'nav': {'propertymapping': '属性设置'}}
								}
	return render(request, 'index.html', {'menu_dict': menu_dict})

def home(request):
	sensors = models.sensors.objects.order_by('type').order_by('sensor_code').all()
 
	return render(request, 'home.html', {'sensors': sensors})

def equipments(request):
	return render(request, 'equipments.html')

def sensors(request):
	#获取所有传感器类别
	sensor_type = models.propertymapping.objects.order_by('property_name').filter(property_name='sensor_type').all()
	#for i in sensor_type:
	#	print(i.id)
	return render(request, 'sensors.html', {'sensor_type':sensor_type})

def pins(request):
	return render(request, 'pins/index.html')
	
def propertymapping(request):
	return render(request, 'propertymapping/index.html')

def ultrasonic(request):
	return render(request, 'ultrasonic/index.html')

def smoke(request):
	return render(request, 'smoke/index.html')

def fire(request):
	return render(request, 'fire/index.html')

def light(request):
	return render(request, 'light/index.html')
	
def led(request):
	return render(request, 'led/index.html')

def soil(request):
	return render(request, 'soil/index.html')

def rain(request):
	return render(request, 'rain/index.html')
	
def relay(request):
	return render(request, 'relay/index.html')

def dht11(request):
	return render(request, 'dht11/index.html')

def activebuzzer(request):
	return render(request, 'activebuzzer/index.html')

def sound(request):
	return render(request, 'sound/index.html')

def obstacleavoidance(request):
	return render(request, 'obstacleavoidance/index.html')

def aroadtracing(request):
	return render(request, 'aroadtracing/index.html')

def infraredemission(request):
	return render(request, 'infraredemission/index.html')

def infraredreception(request):
	return render(request, 'infraredreception/index.html')

def human(request):
	return render(request, 'human/index.html')
	
def current(request):
	return render(request, 'current/index.html')

def show(request):
    tbn = request.GET['tablename']
    search = request.GET['_search']
    nd = request.GET['nd']
    get_rows = request.GET['rows'] 
    get_page = request.GET['page']
    sidx = request.GET['sidx']
    sord = request.GET['sord']  
    page = int(get_page)    
    rows = int(get_rows)
    
    c = "tablename="+tbn+"&search="+search+"&nd="+nd+"&rows="+str(rows)+"&page="+str(page)+"&sidx="+sidx+"&sord="+sord

    if not search.strip():
        search = 'false'
    if not sidx.strip():
        sidx = 'id'
    #判断排序方式是asc 还是 desc
    if operator.eq(sord,'desc'):
        sord = '-'
    else:
        sord = ''
        
    #排序方式为
    order = sord + sidx
    
    if tbn == 'ultrasonic':
        queryset = models.ultrasonic.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.ultrasonic.objects.count()
    elif tbn == 'smoke':
        queryset = models.smoke.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.smoke.objects.count()
    elif tbn == 'fire':
        queryset = models.fire.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.fire.objects.count()
    elif tbn == 'light':
        queryset = models.light.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.light.objects.count()
    elif tbn == 'soil':
        queryset = models.soil.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.soil.objects.count()
    elif tbn == 'rain':
        queryset = models.rain.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.rain.objects.count()
    elif tbn == 'dht11':
        queryset = models.dht11.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.dht11.objects.count()
    elif tbn == 'activebuzzer':
        queryset = models.activebuzzer.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.activebuzzer.objects.count()
    elif tbn == 'sound':
        queryset = models.sound.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.sound.objects.count()
    elif tbn == 'obstacleavoidance':
        queryset = models.obstacleavoidance.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.obstacleavoidance.objects.count()
    elif tbn == 'aroadtracing':
        queryset = models.aroadtracing.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.aroadtracing.objects.count()
    elif tbn == 'infraredemission':
        queryset = models.infraredemission.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.infraredemission.objects.count()
    elif tbn == 'infraredreception':
        queryset = models.infraredreception.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.infraredreception.objects.count()
    elif tbn == 'human':
        queryset = models.human.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.human.objects.count()
    elif tbn == 'pins':
        queryset = models.pins.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.pins.objects.count()
    elif tbn == 'propertymapping':
        queryset = models.propertymapping.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.propertymapping.objects.count()
    elif tbn == 'led':
        queryset = models.led.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.led.objects.count()
    elif tbn == 'relay':
        queryset = models.relay.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.relay.objects.count()
    elif tbn == 'current':
        queryset = models.current.objects.all().order_by(order)[(page-1)*rows: page*rows]
        records = models.current.objects.count()
    else:
        return HttpResponse('error')
  
    json_data = backjson(page,rows,records,queryset)
    return HttpResponse(json_data)



def delete(request):
    tbn = request.GET['tablename']
	
    if tbn == 'ultrasonic':
        queryset = models.ultrasonic.objects.all().delete()
    elif tbn == 'smoke':
        queryset = models.smoke.objects.all().delete()
    elif tbn == 'fire':
        queryset = models.fire.objects.all().delete()
    elif tbn == 'light':
        queryset = models.light.objects.all().delete()
    elif tbn == 'soil':
        queryset = models.soil.objects.all().delete()
    elif tbn == 'rain':
        queryset = models.rain.objects.all().delete()
    elif tbn == 'dht11':
        queryset = models.dht11.objects.all().delete()
    elif tbn == 'activebuzzer':
        queryset = models.activebuzzer.objects.all().delete()
    elif tbn == 'sound':
        queryset = models.sound.objects.all().delete()
    elif tbn == 'obstacleavoidance':
        queryset = models.obstacleavoidance.objects.all().delete()
    elif tbn == 'aroadtracing':
        queryset = models.aroadtracing.objects.all().delete()
    elif tbn == 'infraredemission':
        queryset = models.infraredemission.objects.all().delete()
    elif tbn == 'infraredreception':
        queryset = models.infraredreception.objects.all().delete()
    elif tbn == 'human':
        queryset = models.human.objects.all().delete()
    else:
        return HttpResponse('error')

    json_data = backajax('success','成功删除 '+str(queryset[0])+' 条数据！')
    return HttpResponse(json_data)
    
def getpins(request):
    pins = models.pins.objects.all().order_by('pin')
    sensors = models.sensors.objects.all()
    records = models.pins.objects.all().order_by('pin').count()

    rows = ''
    for pin in pins:
        sensor_new = '' 
        if not pin.BCM is None:
            #print(pin.id, pin.BCM, 'sssssssssssssssssssss')
            for sensor in sensors:
                #print(sensor.pins)
                for temp in sensor.pins.split(','):
                    if temp == str(pin.BCM):
                        #print('find')
                        sensor_new += sensor.sensor_name+','			 
                        
        if pin.pin%2 == 1:
            rows += '{"sensor0": "'+str(sensor_new[:-1])+'", "BCM0": "'+str(pin.BCM or "")+'", "wPi0": "'+ str(pin.wPi or "") + '", "description0":"'+str(pin.description)+'", "pin0":'+str(pin.pin)
        else:
            rows += ', "pin1": '+str(pin.pin)+', "description1": "'+ str(pin.description) + '", "wPi1":"'+str(pin.wPi or "")+'", "BCM1":"'+str(pin.BCM or "")+'", "sensor1": "'+str(sensor_new[:-1])+'"},'

    json_data = '{"page":1, "total":1, "records":'+str(records/2)+', "rows":['+rows[:-1]+']}'
    print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk\n',json_data)
    return HttpResponse(json_data)
 
 
#统一的json返回
def backjson(page,rows,records,queryset):
    data = {
            'page':page,
            'total':math.ceil(records/rows),
            'records':records,
            'rows':[model_to_dict(item) for item in queryset]
        }
    json_data = json.dumps(data, default = __default)
    #print(json_data)
    return json_data

#统一的json返回
def backajax(state,message):
	data = {
             'state':state,
             'message':message
    		}
	json_data = json.dumps(data, default = __default)
	return json_data

def __default(obj):
	if isinstance(obj, datetime):
		return obj.strftime('%Y-%m-%d %H:%M:%S')
	elif  isinstance(obj, date):
		return obj.strftime('%Y-%m-%d')
	else:
		raise TypeError('%r is not JSON serializable' %obj)


def test(state,message):
    return HttpResponse('这是一个测试方法')

