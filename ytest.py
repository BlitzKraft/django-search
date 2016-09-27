from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json


# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

params = {
    'term' : 'food'
}

client = Client(auth)
response = client.search('San Francisco', **params)


for a in response.businesses:
    print a.name

