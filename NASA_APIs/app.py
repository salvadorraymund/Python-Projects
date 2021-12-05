import requests

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)

# use .json() to convert response to a python dictionary
photos = response.json()['photos']
print(f"Found {len(photos)} photos.")
for photo in photos:
	print(f"Photo ID{photo['id']}: {photo['img_src']}")
