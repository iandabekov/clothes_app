from django.contrib import admin

from .models import Category, Clothes

# Register your models here.

admin.site.register(Clothes)
admin.site.register(Category)
