import requests
import json

request_municipality = input("Enter municipality name:")


#retrieve longitude and latitude from municipality name
try:
    request_location = requests.get("https://api.openweathermap.org/geo/1.0/direct?appid=1646dde8b785ada35b1bddfa52ae254b&q=" + request_municipality)
    if request_location.status_code == 200:
        response_location = request_location.json()
        for data in response_location:
            longitude = data["lon"]
            latitude = data["lat"]
        # retrieve weather information from longitude and latitude
        try:
            request_weather = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&appid=1646dde8b785ada35b1bddfa52ae254b")
            if request_weather.status_code == 200:
                response_weather = request_weather.json()
                #print(json.dumps(response_weather, indent=4))
                weather_data = response_weather["current"]["weather"][0]
                description = weather_data['description']
                temperature = int(response_weather["current"]["temp"])
                print(f"Current weather: {description}")
                print(f"Temperature {temperature - 273.15:.2f} Celcius degree")
        except requests.exceptions.RequestException as error:
            print("Error", error)
except requests.exceptions.RequestException as e:
     print(e, "The request can not be executed")


