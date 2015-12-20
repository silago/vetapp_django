from django.conf.urls import url
from django.contrib import admin
from base import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^category/([\w-]+)/$',views.category), 
    url(r'^product/([\w-]+)/$',views.product), 
    url(r'^basket/put/([\d]+)/([\d]+)/$',views.basket_put), 
    url(r'^basket/get/([\d]+)/$',views.basket_get), 
    url(r'^basket/delete/([\d]+)/$',views.basket_delete), 
    url(r'^$',views.index), 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)



