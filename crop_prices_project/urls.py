# crop_prices_project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('crop_prices/', include('crop_prices_app.urls')),
]
