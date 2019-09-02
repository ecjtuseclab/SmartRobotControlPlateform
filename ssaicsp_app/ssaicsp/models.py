from django.db import models

# Create your models here.
class equipments(models.Model):
    rpi_code = models.CharField(max_length=20)
    rpi_name = models.CharField(max_length=20)
    remote_serverhost = models.CharField(max_length=20)
    remote_serverport = models.IntegerField() 
    local_serverhost = models.CharField(max_length=20)
    local_serverport = models.IntegerField() 
    local_servermaxconcount = models.IntegerField() 
    local_clientcount = models.IntegerField() 
    sendtime = models.IntegerField() 
    checkcontime = models.IntegerField() 
    equipmentInfos = models.CharField(max_length=255,null=True)
    equipmentkey = models.CharField(max_length=255,null=True)
    r1 = models.CharField(max_length=255,null=True)
    r2 = models.CharField(max_length=255,null=True)
    create_time = models.DateTimeField()
    remark = models.CharField(max_length=200,null=True)
    status = models.IntegerField()
    
    def __unicode__(self):  # __str__ on Python 3
        return self.rpi_code

class sensors(models.Model):
	rpi_code = models.CharField(max_length=20)
	sensor_code = models.CharField(max_length=3)
	sensor_name = models.CharField(max_length=20)
	type = models.IntegerField() 
	acqfre  = models.FloatField() 
	tranfre  = models.FloatField() 
	enable  = models.IntegerField() 
	keep_time = models.IntegerField()
	rediscount = models.IntegerField()
	pins = models.CharField(max_length=50)
	parameters = models.CharField(max_length=100)
	create_time = models.DateTimeField()
	remark = models.CharField(max_length=200,null=True)
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.sensor_code

class pins(models.Model):
	pin = models.IntegerField() 
	wPi = models.IntegerField() 
	BCM = models.IntegerField() 
	description = models.CharField(max_length=20)
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.pin
		
class propertymapping(models.Model):
	property_name = models.CharField(max_length=20)
	property_value = models.CharField(max_length=20)
	property_meaning = models.CharField(max_length=50)
	remark = models.CharField(max_length=255)
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.property_name	

class 	ultrasonic(models.Model):
	sensor_code = models.CharField(max_length=3)
	distance = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.distance

class 	smoke(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_smoke = models.IntegerField() 
	smoke_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_smoke

class 	fire(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_fire = models.IntegerField() 
	fire_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_fire

class 	light(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_light = models.IntegerField() 
	light_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_light
		
class 	led(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_led = models.IntegerField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_led

class 	soil(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_soil = models.IntegerField() 
	soil_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_soil

class 	rain(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_rain = models.IntegerField()  
	rain_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_rain
		
class 	current(models.Model):
	sensor_code = models.CharField(max_length=3)
	current_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.current_value

class 	relay(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_relay = models.IntegerField()  
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_rain
		
class 	dht11(models.Model):
	sensor_code = models.CharField(max_length=3)
	temperature = models.FloatField() 
	humidity = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.temperature

class 	activebuzzer(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_activebuzzer = models.IntegerField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_activebuzzer

class 	sound(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_sound = models.IntegerField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_sound 

class 	obstacleavoidance(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_obstacleavoidance = models.IntegerField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_obstacleavoidance

class 	aroadtracing(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_aroadtracing = models.IntegerField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_aroadtracing

class 	infraredemission(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_infraredemission = models.IntegerField() 
	infraredemission_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_infraredemission

class 	infraredreception(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_infraredreception = models.IntegerField() 
	infraredreception_value = models.FloatField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_infraredreception

class 	human(models.Model):
	sensor_code = models.CharField(max_length=3)
	is_human = models.IntegerField() 
	create_time = models.DateTimeField()
	status = models.IntegerField()

	def __unicode__(self):  # __str__ on Python 3
		return self.is_human

