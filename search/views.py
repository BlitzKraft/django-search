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
    search_query = forms.CharField(label = '')

def index(request):
    form = searchForm()
    template = loader.get_template(os.path.join(CURR_PATH, 'search/templates/search/index.html'))
    context = { 'form' : form,
               }

    return HttpResponse(template.render(context, request))

def search_res(in_text):
    query = in_text.POST['search_query']
    if(query== ''):
        return HttpResponse(template.render(context, request))
    result = search_yelp(query)
    form = searchForm(initial={'search_query': query })
    template = loader.get_template(os.path.join(CURR_PATH, 'search/templates/search/index.html'))
    context = { 
                'form' : form,
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
        if a.image_url is None:
            a.image_url = 'http://http.cat/404.jpg'
        out.append([a.name, a.image_url.replace("ms.jpg", "l.jpg"), a.url ])
    if (len(out) == 0):
        out.append('No results found')
    return out

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
