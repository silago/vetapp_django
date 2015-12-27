from django.shortcuts import render
import uuid
from django.core.context_processors import csrf
from django.http import Http404, JsonResponse
from django.shortcuts import render_to_response
from base.models import Category, Product, BasketProduct, SessionBasket, Order, OrderProducts 
import json
from django.contrib.sessions.backends.db import SessionStore
from functools import wraps
from datetime import datetime, timedelta
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect
DAYS_BASKET_LIFETIME = 2

def check_session_decorator(function):
    @wraps(function)
    def decorator(request, *args, **kwargs):
        if ( not request.session.session_key):
            request.session = SessionStore()
            request.session.save()
        return function(request, *args, **kwargs)
    return decorator


def get_menu(parent = False):
    #result = [{'item':{},'children':[]}]
    result = []
    if (not parent):
        data = Category.objects.filter(parent__isnull=True)
    else:
        data = Category.objects.filter(parent=parent)
    for item in data:
        result.append({
            'item':item,
            'children':get_menu(item),
            })
    return result


@check_session_decorator
def index(request):
    data = {}
    data['products']   = Product.objects.all().order_by('creation_ts')[:14]
    data['menu']     = get_menu(False)
    return render_to_response('index.html',{'data':data})

def category(request,cslug):
    data = {}
    category = Category.objects.get(slug=cslug)
    data['category'] = category
    data['menu']     = get_menu(False)
    data['categories']     = Category.objects.all()
    data['products'] = Product.objects.filter(Q(category__in=Category.objects.filter(parent=category)) | Q (category=category)  )
    return render_to_response('category.html',{'data':data})

def product(request,pslug):
    data = {}
    data['menu']     = get_menu(False)
    data['product'] = Product.objects.get(slug=pslug)
    return render_to_response('product.html',{'data':data})

@check_session_decorator
def basket(request):
    basket = get_session_basket(request.session.session_key)
    result = []
    for r in BasketProduct.objects.filter(session=basket):
        try:
            item = Product.objects.get(pk=r.product_id)
        except:
            r.delete()
            continue
        res = {}
        res['quantity'] = str(r.quantity)
        res['price'] = item.price
        res['id'] = item.id
        res['title'] = item.title 
        res['total'] = item.price*r.quantity
        res['slug']  = item.slug 
        result.append(res)
    data={'basket':result}
    data['menu']     = get_menu(False)
    return render_to_response('basket.html',{'data':data})


@csrf_protect
def checkout(request):
    data = {}
    if request.method=='POST':
        input_data = request.POST
        errors = []
        for key in ['name','phone','address','email']:
            if key not in input_data or not input_data[key]:
                errors.append(key)
        if (len(errors)>0):
            data['errors'] = errors
            return render_to_response('checkout.html',{'data':data})
        uid = False
        while (not uid or Order.objects.filter(uid=uid).count()):
            uid = uuid.uuid4().hex
        order = Order(uid = uid,name=input_data['name'],email=input_data['email'],address=input_data['address'],phone=input_data['phone'],comment=input_data['comment'] or '')
        order.save()
        data['order'] = order
        basket = get_session_basket(request.session.session_key)
        products = BasketProduct.objects.filter(session=basket)
        for prod in products:
            OrderProducts(order=order,product_id=prod.product_id,quantity=prod.quantity).save()
        basket.delete()
        return render_to_response('checkout_ok.html',{'data':data})
    if request.method=='GET':
        c = {}
        c.update(csrf(request))
        return render_to_response('checkout.html',c)


def get_session_basket(session_key):
    try:
        session_basket = SessionBasket.objects.filter(session_key=session_key).first()
    except:
        #basket no found
        session_basket = None
    if (session_basket):
        if session_basket.creation_ts < (datetime.now() - timedelta(days=DAYS_BASKET_LIFETIME)).date():
            BasketProduct.objects.filter(session=session_basket).delete()
            #BasketProduct.save()
            session_basket.creation_ts = datetime.now()
            session_basket.save()
    else: 
        session_basket = SessionBasket(session_key=session_key)
        session_basket.save()
    return session_basket

def search(request,q):
    data = {}
    data['products'] = Product.objects.filter(title__contains=q)
    return render_to_response('search.html',{'data':data})
    

def order(request,order_uid):
    try:
        order = Order.objects.get(uid=order_uid)
        return render_to_response('order.html',{'data':order})
    except:
        return render_to_response('404.html',{})

@check_session_decorator
def basket_delete(request,product_id):
    basket = get_session_basket(request.session.session_key)
    item = BasketProduct.objects.filter(session=basket,product_id=product_id).delete()
    result = [{'product_id':p.product_id, 'quantity':p.quantity} for p in list( BasketProduct.objects.filter(session=basket))]
    return JsonResponse({'status':'ok','data':result})

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
def basket_get(request):
    basket = get_session_basket(request.session.session_key)
    result = [{'product_id':p.product_id, 'quantity':p.quantity} for p in list( BasketProduct.objects.filter(session=basket))]
    return JsonResponse({'status':'ok','data':result})


