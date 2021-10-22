import requests

API_KEY = "HkTcjCJipKf7K3f72EYsv53ltYEKMfkR"
endpoint = "https://api.giphy.com/v1/gifs/search"

search_term ="kobe"
params = {"api_key": API_KEY, "limit": 1, "q":search_term, "rating":"g"}
response = requests.get(endpoint, params=params).json()
for gif in response['data']:
	title = gif['title']
	url = gif['url']
	print(f'{title} | {url}')