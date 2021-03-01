import requests

def get_info_weather():
    api_key = ''
    city_id = '3462315'
    url = f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}'

    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    print(get_info_weather())