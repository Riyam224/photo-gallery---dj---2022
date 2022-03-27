from atexit import register
from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import Photo , Category


admin.site.register(Photo)
admin.site.register(Category)