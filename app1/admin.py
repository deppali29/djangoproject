from django.contrib import admin
from app1.models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['title']


    prepopulated_fields={ 'slug':('title',)  }



admin.site.register(Product,ProductAdmin)