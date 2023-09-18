from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('burgerapp/', include('burgerapp.urls')),
]
