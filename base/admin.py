from django.contrib import admin
from base.models import Category

class CategoryAdmin(admin.ModelAdmin):
        pass
admin.site.register(Category,CategoryAdmin)

# Register your models here.
