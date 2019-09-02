"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from ssaicsp import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index, name='index'),
	path('home', views.home, name='home'),
	path('equipments', views.equipments, name='equipments'),
	path('sensors', views.sensors, name='sensors'),
	path('pins', views.pins, name='pins'),
	path('propertymapping', views.propertymapping, name='propertymapping'),
	path('ultrasonic', views.ultrasonic, name='ultrasonic'),
	path('smoke', views.smoke, name='smoke'),
	path('fire', views.fire, name='fire'),
	path('light', views.light, name='light'),
	path('led', views.led, name='led'),
	path('soil', views.soil, name='soil'),
	path('rain', views.rain, name='rain'),
	path('relay', views.relay, name='relay'),
	path('dht11', views.dht11, name='dht11'),
	path('activebuzzer', views.activebuzzer, name='activebuzzer'),
	path('sound', views.sound, name='sound'),
	path('obstacleavoidance', views.obstacleavoidance, name='obstacleavoidance'),
	path('aroadtracing', views.aroadtracing, name='aroadtracing'),
	path('infraredemission', views.infraredemission, name='infraredemission'),
	path('infraredreception', views.infraredreception, name='infraredreception'),
	path('human', views.human, name='human'),
	path('current', views.current, name='current'),

	path('show', views.show, name='show'),
	path('delete', views.delete, name='delete'),

	path('getequipments', views.getequipments, name='getequipments'),
	path('editequipments', views.editequipments, name='editequipments'),
	path('getsensors', views.getsensors, name='getsensors'),
	path('editsensors', views.editsensors, name='editsensors'),
	path('restartequipments', views.restartequipments, name='restartequipments'),
	path('getpins', views.getpins, name='getpins'),
	path('controlsensor', views.controlsensor, name='controlsensor'),

    path('test', views.test, name='test'),
]
