from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from base.models import *

def index(request):
    return render_to_response('index.html')

    pass

# Create your views here.
