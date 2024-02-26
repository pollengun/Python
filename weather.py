import requests

api_key='cae1880ee2e1586dde05173a0ba76889'

user_input=input('Enter your city: ')

weatherData=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}')

temp=weatherData.json()['main']['temp']
celsius= round(temp- 273.15,2)

clouds= weatherData.json()['weather'][0]['description']

print(f'Temperature = {celsius} celsius')
print(f'Sky = {clouds}')