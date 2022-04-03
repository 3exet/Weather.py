import pyowm
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM('c7765613f34f42346f01804b72372fb4', config_dict)
mgr = owm.weather_manager()
place=input('Введите ваш город/страну:')
observation = mgr.weather_at_place(place)
w = observation.weather
temp=w.temperature('celsius')['temp']
print("В городе "+place+" сейчас "+w.detailed_status)
print("Температура сейчас в районе "+str(temp))
input()    
