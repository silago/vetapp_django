from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.shortcuts import render_to_response
from base.models import Category, Product, BasketProduct, SessionBasket 
import json
from django.contrib.sessions.backends.db import SessionStore
from functools import wraps
from datetime import datetime, timedelta
from django.db.models import Q
DAYS_BASKET_LIFETIME = 2

def check_session_decorator(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if ( not request.session.session_key):
            request.session = SessionStore()
            request.session.save()
        return function(request, *args, **kwargs)
    return decorator

@check_session_decorator
def index(request):
    data = {}
    data['latest'] = Product.objects.all().order_by('creation_ts')[:4]
    data['products'] =  Product.objects.all().order_by('creation_ts')[4:10]
    return render_to_response('index.html',{'data':data})

def category(request,cslug):
    data = {}
    category = Category.objects.get(slug=cslug)
    data['category'] = category
    data['categories']     = Category.objects.all()
    data['products'] = Product.objects.filter(Q(category__in=Category.objects.filter(parent=category)) | Q (category=category)  )
    return render_to_response('category.html',{'data':data})

def product(request,pslug):
    data = {}
    data['product'] = Product.objects.get(slug=pslug)
    return render_to_response('product.html',{'data':data})



def get_session_basket(session_key):
    try:
        session_basket = SessionBasket.objects.filter(session_key=session_key).first()
    except:
        #basket no found
        session_basket = None
    if (session_basket):
        if session_basket.creation_ts < (datetime.now() - timedelta(days=DAYS_BASKET_LIFETIME)).date():
            BasketProduct.objects.filter(session=session_basket).delete()
            BasketProduct.save()
    else: 
        session_basket = SessionBasket(session_key=session_key)
        session_basket.save()
    return session_basket

@check_session_decorator
def basket_put(request,product_id,quantity):
    basket = get_session_basket(request.session.session_key)
    item = BasketProduct.objects.filter(session=basket,product_id=product_id).first()
    if (item):
        item.quantity+=int(quantity)
        item.save()
    else:
        BasketProduct.objects.create(session=basket,product_id=product_id,quantity=quantity)
    result = [{'product_id':p.product_id, 'quantity':p.quantity} for p in list( BasketProduct.objects.filter(session=basket))]
    return JsonResponse({'status':'ok','data':result})

@check_session_decorator
def basket_get():
    user_id = request.user.user_id
    if (not user_id): return JsonResponse({'status':'NotFound'})
    result = BasketProduct.objects.filter(user=user_id)
    return JsonResponse({'status':'ok','data':json.dumps(result)})

def basket_delete(produt_id):
    user = request.user.id
    pass

