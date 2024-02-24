import requests
import geocoder
import json


#finds client's location
g_local = geocoder.ip('me')
c_local = g_local.latlng
#gathers data from the client's location
#Air Quality 
payload = {'lat':c_local[0],'lon':c_local[1],'appid':'c83ea58166152328bd90438752d76fe2'}
aq = requests.get('http://api.openweathermap.org/data/2.5/air_pollution?',payload)
data_aq = aq.json()
#Weather
wthr = requests.get('https://api.openweathermap.org/data/2.5/weather?',payload)
data_wthr = wthr.json()
#temperture
data_temp = data_wthr['main']['temp']
#Rainfall
r = requests.get('https://api.openweathermap.org/data/2.5/forecast?',payload)
data_r = r.json()
data_rf = data_r['list'][7]['pop']
#Windspeed
data_ws = data_wthr['wind']['speed']
