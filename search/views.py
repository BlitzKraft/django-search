from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaulttags import csrf_token
from django.template import loader
from django.shortcuts import render
from django import forms
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import io
import json

import os

CURR_PATH = os.path.abspath('./')
result = ''

class searchForm(forms.Form):
    title = forms.CharField(label = '')

def index(request):
    form = searchForm()
    template = loader.get_template(os.path.join(CURR_PATH, 'search/templates/search/index.html'))
    context = { 'form' : form,
               }

    return HttpResponse(template.render(context, request))

def search_res(in_text):
    form = searchForm()
    result = search_yelp(in_text.POST['title'])
    template = loader.get_template(os.path.join(CURR_PATH, 'search/templates/search/index.html'))
    context = { 'form' : form,
                'res' : result,
               }

    return HttpResponse(template.render(context, in_text))


def search_yelp(input):
    out = []
    with io.open('config_secret.json') as cred:
        creds = json.load(cred)
        auth = Oauth1Authenticator(**creds)
        client = Client(auth)

    params = {
        'term' : input
    }

    client = Client(auth)
    response = client.search('Atlanta', **params)


    for a in response.businesses:
        out.append(a.name)
    if (len(out) == 0):
        out.append('No results found')
    return out

