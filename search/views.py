from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django import forms
import os

CURR_PATH = os.path.abspath('./')

class searchForm(forms.Form):
    title = forms.CharField(max_length=100)

def index(request):
    form = searchForm()
    template = loader.get_template(os.path.join(CURR_PATH, 'search/templates/search/index.html'))

    #return HttpResponse("This is the search index.")
    return HttpResponse(template.render())


