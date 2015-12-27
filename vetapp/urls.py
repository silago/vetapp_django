from django.conf.urls import url, include
from django.contrib import admin
from base import views as base_views
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.flatpages import views

urlpatterns = [
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^basket/$',                       base_views.basket), 
    url(r'^checkout/$',                      base_views.checkout), 
    url(r'^category/([\w-]+)/$',            base_views.category), 
    url(r'^product/([\w-]+)/$',             base_views.product), 
    url(r'^basket/put/([\d]+)/([\d-]+)/$',   base_views.basket_put), 
    url(r'^basket/get/$',           base_views.basket_get), 
    url(r'^order/status/([\w-]+)/$',           base_views.order), 
    url(r'^basket/delete/([\d]+)/$',        base_views.basket_delete), 
    url(r'^$',                              base_views.index), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)



