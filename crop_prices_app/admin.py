# crop_prices_app/admin.py
from django.contrib import admin
from .models import Crop, Price

admin.site.register(Crop)
admin.site.register(Price)
