import requests
import pprint
import random

response = requests.post("https://api.yelp.com/oauth2/token", data = {
	'grant_type': "client_credentials",
	"client_id": "qGN0-clZVHgIJQW4eEZVgA",
	"client_secret": "gDeyt0187jMBS9FWhBKDWkXycsyz174jUeIhCFEUiuJQy4Xr2UfMvX46KMASoPZz"
})


access_token = response.json()['access_token']

search = requests.get("https://api.yelp.com/v3/businesses/search?term=food&location=san+jose", headers = {
	"Authorization": "Bearer %s" % access_token
})

choices = (search.json())

choice_list = choices['businesses'] 

# pprint.pprint(random.choice(choice_list))

destination = random.choice(choice_list)

# name = destination['name']

pprint.pprint(destination)
