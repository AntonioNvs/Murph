import requests

apiKey = ""

def news():
    url = ('http://newsapi.org/v2/top-headlines?'
           'country=br&'
           'apiKey={apiKey}')
    response = requests.get(url)

    return response.json()['articles']


if __name__ == '__main__':
    news()
