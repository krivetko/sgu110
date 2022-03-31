from django.contrib import admin

# Register your models here.
from .models import TileImage, Category
admin.site.register(TileImage)
admin.site.register(Category)
