import requests


API_KEY = "U9Ml7a9ACwzSeq9ysFWl66zFA8FoHXvQ",
language = "en-us",
details = True,
metric = True


def get_city_search():
    city_name = input("Text to search: ")
    query_params = {"apikey": API_KEY,
                    "q": city_name,
                    "language": language,
                    "details": True}

    endpoint = "http://dataservice.accuweather.com/locations/v1/cities/search"
    response = requests.get(endpoint, params=query_params).json()
    return response[0]['Key']


def one_day_forecast(unique_id=None):
    query_params = {"apikey": API_KEY,
                    "language": language,
                    "details": True,
                    "metric": True}

    endpoint = f"http://dataservice.accuweather.com/forecasts/v1/daily/1day/{unique_id}"
    response = requests.get(endpoint, params=query_params).json()
    return response["DailyForecasts"][0]["RealFeelTemperature"]


if __name__ == "__main__":
    my_city_key = get_city_search()
    print(f"The city key I'm looking for is {my_city_key}")
    forecast = one_day_forecast(unique_id=my_city_key)
    print(f"Temperature today is {forecast}")
