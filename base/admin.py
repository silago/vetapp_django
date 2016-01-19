from django.contrib import admin
from base.models import Category, Product
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class CategoryAdmin(admin.ModelAdmin):
        pass
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
        pass
admin.site.register(Product,ProductAdmin)

# Register your models here.

class PageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content' : TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }
        fields = "__all__"


class PageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = PageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
