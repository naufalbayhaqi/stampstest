import requests
from datetime import datetime

def get_weather_forecast():
    api_key = 'b62ed6bd995c3bfe5308546be037e027'
    city = 'Jakarta'
    
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    # print(url)
    try:
        response = requests.get(url)
        
        data = response.json()
        
        daily_forecast = {}
        
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).date()
            
            if date not in daily_forecast:
                daily_forecast[date] = {
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description']
                }
        
        print("Weather Forecast:")
        for date, weather in list(daily_forecast.items())[:5]:
            formatted_date = date.strftime('%a, %d %b %Y')
            print(formatted_date + ": " + f"{weather['temp']}°C")
            
    except Exception as e:
        print(f"Error, {e}")

get_weather_forecast()
