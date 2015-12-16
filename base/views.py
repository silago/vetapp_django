from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from base.models import Category, Product

def index(request):
    data = {}
    data['latest'] = Product.objects.all().order_by('creation_ts')[:4]
    data['products'] =  Product.objects.all().order_by('creation_ts')[4:10]
    return render_to_response('index.html',{'data':data})

    pass

# Create your views here.
