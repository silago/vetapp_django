from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from base.models import *

def index(request):
    return render_to_response('index.html')

    pass


def category(request,cslug):
    data = []
    data['category'] = Category.objects.get(cslug=slug)
    data['products'] = Product.objects.filter(category=category_id)
    return render_to_response('category.html',{data:data})


def product(request,cslug,islug):
    pass
# Create your views here.
