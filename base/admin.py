from django.contrib import admin
from base.models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
        pass
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
        pass
admin.site.register(Product,ProductAdmin)

# Register your models here.
