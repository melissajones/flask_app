from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Function that passes term and location to Yelp API
# and returns a list with business name, rating, phone, and Yelp url.
def get_businesses (term, location):
	auth = Oauth1Authenticator(
		consumer_key=environ['YELP_CONSUMER_KEY'],
		consumer_secret=environ['YELP_CONSUMER_SECRET'],
		token=environ['YELP_TOKEN'],
		token_secret=environ['YELP_TOKEN_SECRET']
	)

	client = Client(auth)

	params = {
		'term': term,
		'lang': 'en',
		'limit': 3 # limits response to 3 results
	}

	response = client.search(location, **params)

	businesses = []
		
	for business in response.businesses:
		#print(business.name, business.rating, business.phone)
		businesses.append({"name": business.name, 
			"rating": business.rating,
			"display_phone": business.display_phone,
			"url": business.url
		})

	return businesses