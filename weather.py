import pyowm

city = input('Какой город вас интересует?: ')



owm = pyowm.OWM('ef282cf7a6c4af7dd3ea64f517bf8421')  # You MUST provide a valid API key
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']
wind = w.get_detailed_status()
print ('В городе ' + city + ' сейчас температура: ' + str(temperature) + ' C')
print ('В городе ' + city + ' погода: ' + wind)

print ('\nПрограмм завершена !')

input()
