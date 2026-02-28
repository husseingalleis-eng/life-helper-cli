import requests

def is_valid_url(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code 
    except requests.RequestException:
        return False
    
def weather_checker():
    print("\nWelcome to Weather Checker (API)\n")
    while True:
        try:
            
            
            ip_api = "http://ip-api.com/json/?fields=61439"
            response_city = requests.get(ip_api)
            city_2 = response_city.json()
            city_2 = city_2["city"]
            city = input("Is this city right? ("+city_2+"): ")
            if city == "no":
                city = input("enter ur city: ")

            if not city:
                raise ValueError('empty string')
            break
        except ValueError as e:
            print(e)
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = 'write your own API key here please so the project can work for you '
    params = {
    "q": city,
    "appid": api_key
    }
    
    response = requests.get(api_url, params= params)

    print(f"Code status is: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        
        print(f"City: {data['name']} ({data['sys']['country']})")
        print(f"Coordinates: {data['coord']['lat']}, {data['coord']['lon']}")
        print(f"Weather: {data['weather'][0]['main']} - {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']} K")
        print(f"Feels Like: {data['main']['feels_like']} K")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        print(f"Cloudiness: {data['clouds']['all']}%")
        print(f"Visibility: {data['visibility']} meters")
    else:
        print("Error:", response.status_code)
        print(response.text)

    