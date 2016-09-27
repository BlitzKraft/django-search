from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django import forms
import os

CURR_PATH = os.path.abspath('./')
result = 'test'

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
    result = in_text
    template = loader.get_template(os.path.join(CURR_PATH, 'search/templates/search/index.html'))
    context = { 'form' : form,
                'res' : result,
               }

    return HttpResponse(template.render(context))
