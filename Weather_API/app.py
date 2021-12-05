import requests


API_KEY = "U9Ml7a9ACwzSeq9ysFWl66zFA8FoHXvQ"
language = "en-us"
query_params = {"apikey": API_KEY, "language": language}
region = "PH"
endpoint = f"http://dataservice.accuweather.com/locations/v1/adminareas/{region}"
responses = requests.get(endpoint, params=query_params).json()
for response in responses:
    if response["ID"] == 'MNL':
        print(response)
