#TASK 4 - WEATHER FORECAST - CodSoft Pvt. Ltd
#Import Libraries
import requests
import tkinter
import time
import cred

#FUNCTION => To Fetch the Weather Details from OpenWeather API
def Weather(self):
    cityname = textfield.get()
    api = 'https://api.openweathermap.org/data/2.5/weather?q='+cityname+'&appid='+cred.keyID
    data = requests.get(api).json()
    weathercondition = data['weather'][0]['main']
    weatherdescription = str(data['weather'][0]['description'])
    temperature = int(data['main']['temp'] - 273.15)
    maxTemp = int(data['main']['temp_max'] - 273.15)
    minTemp = int(data['main']['temp_min'] - 273.15)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    windSpeed = data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(data['sys']['sunset'] - 21600))

    info = weathercondition + '\n' + str(temperature) + '°C' 
    dataresult = '\n'+ 'DESCRIPTION : ' + str(weatherdescription) + '\n' + 'MAXIMUM TEMPERATURE : ' + str(maxTemp) + '°C' + '\n' + 'MINIMUM TEMPERATURE : ' + str(minTemp) + '°C' + '\n\n' + 'HUMIDITY : ' + str(humidity) + ' %' + '\n'+ 'PRESSURE : ' + str(pressure) + ' hPa' + '\n' + 'WIND SPEED : ' + str(windSpeed) + ' km/h' + '\n\n' + 'SUNRISE : ' + str(sunrise) + '\n' + 'SUNSET : ' + str(sunset)
    
    text1.config(text = info)
    text2.config(text= dataresult)

    print(info,dataresult)

    #Too get the Icon Field from the API
    weatherIcon = data['weather'][0]['icon']
    FetchIcon(weatherIcon)

#To fetch the ICON field from the API
def FetchIcon(icon_code):
    iconUrl = f"http://openweathermap.org/img/w/{icon_code}.png"
    iconResponse = requests.get(iconUrl)
    iconImage = tkinter.PhotoImage(data=iconResponse.content)
    text0.configure(image=iconImage)
    text0.image = iconImage  

#For Application Window Siaze
frame = tkinter.Tk()
frame.geometry('450x470')
frame.title('WEATHER CASTER')
frame.iconbitmap('./weather-app.ico')
frame.configure(bg='light blue')

#Variables fontProperty and textProperty used for font styling
fontProperty = ('Eras Bold ITC', 12)
textProperty = ('Eras Bold ITC', 35)

#TextField Property
textfield = tkinter.Entry(frame, font= textProperty, justify='center')
textfield.pack(pady=10)
textfield.focus()
textfield.bind('<Return>', Weather)

#For Output
#Text0 = To display the Icon of Weather
text0 = tkinter.Label(frame)
text0.configure(bg='light blue')
text0.pack()


#Text1 = Weather Report - Weather Cloudy, Mist or else
text1 = tkinter.Label(frame, font=textProperty)
text1.configure(bg='light blue')
text1.pack()

#Text2 = Other Information related to Searched City or States
text2 = tkinter.Label(frame, font=fontProperty)
text2.configure(bg='light blue')
text2.pack()

#To make frame visible
frame.mainloop()
