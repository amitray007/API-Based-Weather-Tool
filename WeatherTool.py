import requests
from os import system
import os
from time import sleep
import json
import datetime  

Initials = '''\n
\t\t\t██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
\t\t\t██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
\t\t\t██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
\t\t\t██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
\t\t\t╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║
\t\t\t ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\n\t\t\t\t Created By : GitHub | amitray007\n
'''

currentTime = datetime.datetime.now() 
currentMonth = currentTime.month
currentYear = currentTime.year
currentDate = currentTime.day

class Weather:
    def __init__(self):
        sleep(1)
        _ = system('cls')
        print(Initials)

    def realtimeWeather(apiKey):
        print(' [+] Realtime Weather Stats')
        query = str(input('\n [+] Enter City Name : '))
        url = 'https://api.weatherapi.com/v1/current.json?key=' + apiKey + '&q=' + query
        response = requests.get(url)
        data = response.text
        parsedData = json.loads(data)

        print('\n [+] Location Data\n --------------------------')
        print(' [++] City : {}'.format(parsedData["location"]["name"]))
        print(' [++] Region : {}'.format(parsedData["location"]["region"]))
        print(' [++] Country : {}'.format(parsedData["location"]["country"]))
        print(' [++] Latitude : {}'.format(parsedData["location"]["lat"]))
        print(' [++] Longitude : {}'.format(parsedData["location"]["lon"]))
        print(' [++] Timezone : {}'.format(parsedData["location"]["tz_id"]))
        print(' [++] Local Time : {}'.format(parsedData["location"]["localtime"]))

        print('\n [+] Weather Report\n --------------------------')
        print(' [++] Last Updated : {}'.format(parsedData["current"]["last_updated"]))
        print(' [++] Tempreature (In Celsius) : {}'.format(parsedData["current"]["temp_c"]))
        print(' [++] Tempreature (In Fahrenheit) : {}'.format(parsedData["current"]["temp_f"]))
        print(' [++] Weather : {}'.format(parsedData["current"]["condition"]["text"]))
        print(' [++] Wind (In Miles per Hour) : {}'.format(parsedData["current"]["wind_mph"]))
        print(' [++] Wind (In Kilometer per Hour) : {}'.format(parsedData["current"]["wind_kph"]))
        print(' [++] Wind Degree : {}'.format(parsedData["current"]["wind_degree"]))

        windDirection = str(parsedData["current"]["wind_dir"])
        finalWindDirection = ''
        for i in range(len(windDirection)):
            if windDirection[i] == 'N':
                finalWindDirection = finalWindDirection + 'North '
            elif windDirection[i] == 'S':
                finalWindDirection = finalWindDirection + 'South '
            elif windDirection[i] == 'E':
                finalWindDirection = finalWindDirection + 'East '
            elif windDirection[i] == 'W':
                finalWindDirection = finalWindDirection + 'West '
        print(' [++] Wind Direction : {}'.format(finalWindDirection))
        print(' [++] Pressure (In Millibars) : {}'.format(parsedData["current"]["pressure_mb"]))
        print(' [++] Precipitation (In Millimeters) : {}'.format(parsedData["current"]["precip_mm"]))
        print(' [++] Humidity : {}'.format(parsedData["current"]["humidity"]))
        print(' [++] Tempreature Feels Like (In Celsius) : {}'.format(parsedData["current"]["feelslike_c"]))
        print(' [++] Tempreature Feels Like (In Fahrenheit) : {}'.format(parsedData["current"]["feelslike_f"]))
        print(' [++] UV : {}'.format(parsedData["current"]["uv"]))
        print(' [++] Wind Speed (In Miles per Hour) : {}'.format(parsedData["current"]["gust_mph"]))
        print(' [++] Wind Speed (In Kilometers per Hour) : {}'.format(parsedData["current"]["gust_kph"]))

    def weatherForecast(apiKey):
        print(' [+] Weather Forecast')
        print('\n [+] NOTE : Forecast for 2 Days Will be Displayed')
        query = str(input('\n [+] Enter City Name : '))
        url = 'https://api.weatherapi.com/v1/forecast.json?key=' + apiKey +'&q=' + query + '&days=3'
        response = requests.get(url)
        data = response.text
        parsedData = json.loads(data)

        print('\n [+] Location Data\n --------------------------')
        print(' [++] City : {}'.format(parsedData["location"]["name"]))
        print(' [++] Region : {}'.format(parsedData["location"]["region"]))
        print(' [++] Country : {}'.format(parsedData["location"]["country"]))
        print(' [++] Latitude : {}'.format(parsedData["location"]["lat"]))
        print(' [++] Longitude : {}'.format(parsedData["location"]["lon"]))
        print(' [++] Timezone : {}'.format(parsedData["location"]["tz_id"]))
        print(' [++] Local Time : {}'.format(parsedData["location"]["localtime"]))

        print("\n [+] Today's Report\n --------------------------")
        print(' [++] Last Updated : {}'.format(parsedData["current"]["last_updated"]))
        print(' [++] Tempreature (In Celsius) : {}'.format(parsedData["current"]["temp_c"]))
        print(' [++] Tempreature (In Fahrenheit) : {}'.format(parsedData["current"]["temp_f"]))
        print(' [++] Weather : {}'.format(parsedData["current"]["condition"]["text"]))
        print(' [++] Wind (In Miles per Hour) : {}'.format(parsedData["current"]["wind_mph"]))
        print(' [++] Wind (In Kilometer per Hour) : {}'.format(parsedData["current"]["wind_kph"]))
        print(' [++] Wind Degree : {}'.format(parsedData["current"]["wind_degree"]))

        windDirection = str(parsedData["current"]["wind_dir"])
        finalWindDirection = ''
        for i in range(len(windDirection)):
            if windDirection[i] == 'N':
                finalWindDirection = finalWindDirection + 'North '
            elif windDirection[i] == 'S':
                finalWindDirection = finalWindDirection + 'South '
            elif windDirection[i] == 'E':
                finalWindDirection = finalWindDirection + 'East '
            elif windDirection[i] == 'W':
                finalWindDirection = finalWindDirection + 'West '
        print(' [++] Wind Direction : {}'.format(finalWindDirection))
        print(' [++] Pressure (In Millibars) : {}'.format(parsedData["current"]["pressure_mb"]))
        print(' [++] Precipitation (In Millimeters) : {}'.format(parsedData["current"]["precip_mm"]))
        print(' [++] Humidity : {}'.format(parsedData["current"]["humidity"]))
        print(' [++] Tempreature Feels Like (In Celsius) : {}'.format(parsedData["current"]["feelslike_c"]))
        print(' [++] Tempreature Feels Like (In Fahrenheit) : {}'.format(parsedData["current"]["feelslike_f"]))
        print(' [++] UV : {}'.format(parsedData["current"]["uv"]))
        print(' [++] Wind Speed (In Miles per Hour) : {}'.format(parsedData["current"]["gust_mph"]))
        print(' [++] Wind Speed (In Kilometers per Hour) : {}'.format(parsedData["current"]["gust_kph"]))

        print("\n [+] Forecast for 2 Days\n --------------------------")
        for i in range(1,3):
            print(' [+] Date : {}'.format(parsedData["forecast"]["forecastday"][i]["date"]))
            print(' [++] Max Tempreature (In Celsius) : {}\t\tMax Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["maxtemp_c"],parsedData["forecast"]["forecastday"][i]["day"]["maxtemp_f"]))
            print(' [++] Min Tempreature (In Celsius) : {}\t\tMin Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["mintemp_c"],parsedData["forecast"]["forecastday"][i]["day"]["mintemp_f"]))
            print(' [++] Average Tempreature (In Celsius) : {}\t\tAverage Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["avgtemp_c"],parsedData["forecast"]["forecastday"][i]["day"]["avgtemp_f"]))
            print(' [++] Max Wind Speed (In Miles per Hour) : {}\t\tMax Wind Speed (In Kilometer per Hour) : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["maxwind_mph"],parsedData["forecast"]["forecastday"][i]["day"]["maxwind_kph"]))
            print(' [++] Total Precipitation (In Millimetres) : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["totalprecip_mm"]))
            print(' [++] Average Humidity : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["avghumidity"]))
            
            rainCheck = str(parsedData["forecast"]["forecastday"][i]["day"]["daily_will_it_rain"])
            if rainCheck == 0:
                finalrainCheck = 'No Possibility of Rain'
            else:
                finalrainCheck = rainCheck
            print(' [++] Will it Rain : {}'.format(finalrainCheck))
            print(' [++] Chance of Rain : {} %'.format(parsedData["forecast"]["forecastday"][i]["day"]["daily_chance_of_rain"]))

            snowCheck = str(parsedData["forecast"]["forecastday"][i]["day"]["daily_will_it_snow"])
            if snowCheck == 0:
                finalsnowCheck = 'No Possibility of Snow'
            else:
                finalsnowCheck = snowCheck
            print(' [++] Will it Snow : {}'.format(finalsnowCheck))
            print(' [++] Chance of Snow : {} %'.format(parsedData["forecast"]["forecastday"][i]["day"]["daily_chance_of_snow"]))
            print(' [++] Weather : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["condition"]["text"]))
            print(' [++] UV : {}'.format(parsedData["forecast"]["forecastday"][i]["day"]["uv"]))

            print('\n [+] Astronomy Details\n --------------------------')
            print(' [++] Sunrise Time : {}'.format(parsedData["forecast"]["forecastday"][i]["astro"]["sunrise"]))
            print(' [++] Sunset Time : {}'.format(parsedData["forecast"]["forecastday"][i]["astro"]["sunset"]))
            print(' [++] Moonrise Time : {}'.format(parsedData["forecast"]["forecastday"][i]["astro"]["moonrise"]))
            print(' [++] Moonset Time : {}\n'.format(parsedData["forecast"]["forecastday"][i]["astro"]["moonset"]))
            if i != 2:
                print('\n --------------------------\n --------------------------\n')

    def previousWeatherReport(apiKey):
        print(' [+] Previous Weather Reports')
        query = str(input('\n [+] Enter City Name : '))

        if currentDate > 1 and currentDate < 16:
            noteMonth = currentMonth - 1
        else:
            noteMonth = currentMonth
        print('\n [+] NOTE : Date should be from {}-{}-16 to Present Day'.format(currentYear,noteMonth))
        dateCheck = str(input(' [+] Enter Previous Date (yyyy-MM-dd) : '))
        url = 'https://api.weatherapi.com/v1/history.json?key=' + apiKey + '&q=' + query + '&dt=' + dateCheck
        response = requests.get(url)
        data = response.text
        parsedData = json.loads(data)

        print('\n [+] Location Data\n --------------------------')
        print(' [++] City : {}'.format(parsedData["location"]["name"]))
        print(' [++] Region : {}'.format(parsedData["location"]["region"]))
        print(' [++] Country : {}'.format(parsedData["location"]["country"]))
        print(' [++] Latitude : {}'.format(parsedData["location"]["lat"]))
        print(' [++] Longitude : {}'.format(parsedData["location"]["lon"]))
        print(' [++] Timezone : {}'.format(parsedData["location"]["tz_id"]))
        print(' [++] Local Time : {}'.format(parsedData["location"]["localtime"]))

        print('\n [+] Whole Day Report\n --------------------------')
        print(' [++] Date : {}'.format(parsedData["forecast"]["forecastday"][0]["date"]))
        print(' [++] Max Tempreature (In Celsius) : {}\t\tMax Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["maxtemp_c"],parsedData["forecast"]["forecastday"][0]["day"]["maxtemp_f"]))
        print(' [++] Min Tempreature (In Celsius) : {}\t\tMin Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["mintemp_c"],parsedData["forecast"]["forecastday"][0]["day"]["mintemp_f"]))
        print(' [++] Average Tempreature (In Celsius) : {}\t\tAverage Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["avgtemp_c"],parsedData["forecast"]["forecastday"][0]["day"]["avgtemp_f"]))
        print(' [++] Max Wind Speed (In Miles per Hour) : {}\t\tMax Wind Speed (In Kilometer per Hour) : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["maxwind_mph"],parsedData["forecast"]["forecastday"][0]["day"]["maxwind_kph"]))
        print(' [++] Total Precipitation (In Millimetres) : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["totalprecip_mm"]))
        print(' [++] Average Humidity : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["avghumidity"]))
        print(' [++] Weather : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["condition"]["text"]))
        print(' [++] UV : {}'.format(parsedData["forecast"]["forecastday"][0]["day"]["uv"]))

        print('\n [+] Astronomy Details\n --------------------------')
        print(' [++] Sunrise Time : {}'.format(parsedData["forecast"]["forecastday"][0]["astro"]["sunrise"]))
        print(' [++] Sunset Time : {}'.format(parsedData["forecast"]["forecastday"][0]["astro"]["sunset"]))
        print(' [++] Moonrise Time : {}'.format(parsedData["forecast"]["forecastday"][0]["astro"]["moonrise"]))
        print(' [++] Moonset Time : {}'.format(parsedData["forecast"]["forecastday"][0]["astro"]["moonset"]))
        print(' [++] Moon Phase : {}'.format(parsedData["forecast"]["forecastday"][0]["astro"]["moon_phase"]))
        print(' [++] Moon Illumination : {}'.format(parsedData["forecast"]["forecastday"][0]["astro"]["moon_illumination"]))

        moreCheck = str(input('\n [+] Want to See Time to Time Report for Whole Day [Y/n] : '))
        moreCheck.upper()
        if moreCheck == 'Y':
            print('\n [+] Timely Report\n --------------------------')
            for i in range(0,24):
                print(' [+] Time : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["time"]))
                print(' [++] Tempreature (In Celsius) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["temp_c"]))
                print(' [++] Tempreature (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["temp_f"]))
                print(' [++] Weather : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["condition"]["text"]))
                print(' [++] Wind (In Miles per Hour) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["wind_mph"]))
                print(' [++] Wind (In Kilometer per Hour) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["wind_kph"]))
                print(' [++] Wind Degree : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["wind_degree"]))

                windDirection = str(parsedData["forecast"]["forecastday"][0]["hour"][i]["wind_dir"])
                finalWindDirection = ''
                for i in range(len(windDirection)):
                    if windDirection[i] == 'N':
                        finalWindDirection = finalWindDirection + 'North '
                    elif windDirection[i] == 'S':
                        finalWindDirection = finalWindDirection + 'South '
                    elif windDirection[i] == 'E':
                        finalWindDirection = finalWindDirection + 'East '
                    elif windDirection[i] == 'W':
                        finalWindDirection = finalWindDirection + 'West '
                print(' [++] Wind Direction : {}'.format(finalWindDirection))
                print(' [++] Pressure (In Millibars) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["pressure_mb"]))
                print(' [++] Precipitation (In Millimeters) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["precip_mm"]))
                print(' [++] Humidity : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["humidity"]))
                
                cloudCheck = str(parsedData["forecast"]["forecastday"][0]["hour"][i]["cloud"])
                if cloudCheck == 0:
                    finalcloudCheck = 'No Clouds'
                else:
                    finalcloudCheck = cloudCheck + ' %'
                print(' [++] Cloudy : {}'.format(finalcloudCheck))
                print(' [++] Tempreature Feels Like (In Celsius) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["feelslike_c"]))
                print(' [++] Tempreature Feels Like (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["feelslike_f"]))
                print(' [++] Heat Index (In Celsius) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["heatindex_c"]))
                print(' [++] Heat Index (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["heatindex_f"]))
                print(' [++] Dew Point (In Celsius) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["dewpoint_c"]))
                print(' [++] Dew Point (In Fahrenheit) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["dewpoint_f"]))
                
                rainCheck = str(parsedData["forecast"]["forecastday"][0]["hour"][i]["will_it_rain"])
                if rainCheck == 0:
                    finalrainCheck = 'No Possibility of Rain'
                else:
                    finalrainCheck = rainCheck
                print(' [++] Will it Rain : {}'.format(finalrainCheck))
                print(' [++] Chance of Rain : {} %'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["chance_of_rain"]))

                snowCheck = str(parsedData["forecast"]["forecastday"][0]["hour"][i]["will_it_snow"])
                if snowCheck == 0:
                    finalsnowCheck = 'No Possibility of Snow'
                else:
                    finalsnowCheck = snowCheck
                print(' [++] Will it Snow : {}'.format(finalsnowCheck))
                print(' [++] Chance of Snow : {} %'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["chance_of_snow"]))
                print(' [++] Wind Speed (In Miles per Hour) : {}'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["gust_mph"]))
                print(' [++] Wind Speed (In Kilometers per Hour) : {}\n'.format(parsedData["forecast"]["forecastday"][0]["hour"][i]["gust_kph"]))

    def ipLookup(apiKey):
        print(' [+] IP lookup')
        query = str(input('\n [+] Enter IP Address : '))
        url = 'https://api.weatherapi.com/v1/timezone.json?key=' + apiKey + '&q=' + query
        response = requests.get(url)
        data = response.text
        parsedData = json.loads(data)
        
        print('\n [+] Location Data\n --------------------------')
        print(' [++] City : {}'.format(parsedData["location"]["name"]))
        if parsedData["location"]["region"] != "":
            print(' [++] Region : {}'.format(parsedData["location"]["region"]))
        print(' [++] Country : {}'.format(parsedData["location"]["country"]))
        print(' [++] Latitude : {}'.format(parsedData["location"]["lat"]))
        print(' [++] Longitude : {}'.format(parsedData["location"]["lon"]))
        print(' [++] Timezone : {}'.format(parsedData["location"]["tz_id"]))
        print(' [++] Local Time : {}'.format(parsedData["location"]["localtime"]))

    def locationAstronomy(apiKey):
        print(' [+] Location Astronomy')
        query = str(input('\n [+] Enter City Name : '))
        dateCheck = str(input(' [+] Enter Date (yyyy-MM-dd) : '))
        url = 'https://api.weatherapi.com/v1/astronomy.json?key=' + apiKey + '&q=' + query + '&dt=' + dateCheck
        response = requests.get(url)
        data = response.text
        parsedData = json.loads(data)

        print('\n [+] Location Data\n --------------------------')
        print(' [++] City : {}'.format(parsedData["location"]["name"]))
        print(' [++] Region : {}'.format(parsedData["location"]["region"]))
        print(' [++] Country : {}'.format(parsedData["location"]["country"]))
        print(' [++] Latitude : {}'.format(parsedData["location"]["lat"]))
        print(' [++] Longitude : {}'.format(parsedData["location"]["lon"]))
        print(' [++] Timezone : {}'.format(parsedData["location"]["tz_id"]))
        print(' [++] Local Time : {}'.format(parsedData["location"]["localtime"]))

        print('\n [+] Astronomy Details\n --------------------------')
        print(' [++] Sunrise Time : {}'.format(parsedData["astronomy"]["astro"]["sunrise"]))
        print(' [++] Sunset Time : {}'.format(parsedData["astronomy"]["astro"]["sunset"]))
        print(' [++] Moonrise Time : {}'.format(parsedData["astronomy"]["astro"]["moonrise"]))
        print(' [++] Moonset Time : {}'.format(parsedData["astronomy"]["astro"]["moonset"]))


    def detailsLocation(apiKey):
        print(' [+] Details about a Location')
        query = str(input('\n [+] Enter City Name : '))
        url = 'https://api.weatherapi.com/v1/timezone.json?key=' + apiKey + '&q=' + query
        response = requests.get(url)
        data = response.text
        parsedData = json.loads(data)
        
        print('\n [+] Location Data\n --------------------------')
        print(' [++] City : {}'.format(parsedData["location"]["name"]))
        print(' [++] Region : {}'.format(parsedData["location"]["region"]))
        print(' [++] Country : {}'.format(parsedData["location"]["country"]))
        print(' [++] Latitude : {}'.format(parsedData["location"]["lat"]))
        print(' [++] Longitude : {}'.format(parsedData["location"]["lon"]))
        print(' [++] Timezone : {}'.format(parsedData["location"]["tz_id"]))
        print(' [++] Local Time : {}'.format(parsedData["location"]["localtime"]))

if __name__ == "__main__":
    system('title Weather Tool')
    while True:
        _ = system('cls')
        print(Initials)

        if os.path.exists('./APIkey.txt') is False:
            open('./APIkey.txt','w+')
            data = ''
        else:
            apiFile = open('./APIkey.txt','r')
            data = apiFile.read()

        if len(data) == 31:
            apiKey = open('./APIkey.txt').readline()
            print(' [+] Retreived API key from file')
        else:
            apiCheck = str(input(' [+] Already have an API key [Y/n] : '))
            apiCheck.upper()
            if apiCheck == 'Y':
                apiKey = input(' [+] Enter API Key : ')
                apiFile = open('./APIkey.txt','w')
                apiFile.write('{}'.format(apiKey))
            else:
                print(' [+] Using Default API key!')
                apiKey = '1342ac8f3abc41e68d0152830202205'

        print('\n [+] Authenticating the API key')
        apiValid = False
        while apiValid != True:
            urlCheck = 'https://api.weatherapi.com/v1/current.json?key=' + apiKey
            response = requests.get(urlCheck)

            if response.status_code == 401:
                print(' [+] API key Authentication Failed')
                apiValid = False
            elif response.status_code == 403:
                print(' [+] API key has been disabled or Exceeded Monthly Calls or Internal Error')
                apiValid = False
            else:
                print(' [+] API key Authenticated Successfully')
                apiValid = True

            if apiValid is False:
                apiKey = input(' [+] Enter New API Key : ')

        print('\n [+] Opening Menu ...\n\n [+] Choose from the Menu\n --------------------------')
        print(' [1] Realtime Weather Stats\n [2] Weather Forecast\n [3] Previous Weather Reports\n [4] Location Astronomy\n [5] IP Lookup \n [6] Details about location')
        menuID = int(input('\n [+] Enter your Choice : '))

        while menuID<=0 or menuID>=7:
            print('\n [+] Wrong Operation')
            menuID = int(input(' [+] Enter your Choice Again : '))

        if menuID == 1:
            print('\n [+] Opening Realtime Weather Stats')
            Weather()
            Weather.realtimeWeather(apiKey)
        elif menuID == 2:
            print('\n [+] Opening Weather Forecast')
            Weather()
            Weather.weatherForecast(apiKey)
        elif menuID == 3:
            print('\n [+] Opening Previous Weather Reports')
            Weather()
            Weather.previousWeatherReport(apiKey)
        elif menuID == 4:
            print('\n [+] Opening Location Astronomy')
            Weather()
            Weather.locationAstronomy(apiKey)
        elif menuID == 5:
            print('\n [+] Opening IP Lookup')
            Weather()
            Weather.ipLookup(apiKey)
        else:
            print('\n [+] Opening Location Details')
            Weather()
            Weather.detailsLocation(apiKey)

        repeat = str(input('\n [+] Want to check again [Y/n] : '))
        repeat.upper()

        if repeat == 'Y':
            continue
        else:
            quit()
