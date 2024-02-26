import requests #for request.get() function
import json     #for jason.loads function
import win32com.client as wincom #for speech function
speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the city name :" )
apiKey = 'cae1880ee2e1586dde05173a0ba76889'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}'

r = requests.get(url)
# print (r.text)

conDict = json.loads(r.text) #converts r.text to dictonary
print(f"temprature: { conDict['main']['temp']}")
print(f"clouds: {conDict['weather'][0]['description']}")
print(f"visibility: {conDict['visibility']}")
# speak.Speak(f"The temperature in {city} is {t} celsius and the weather is {weather}.")


