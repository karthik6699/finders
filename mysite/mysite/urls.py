from django.contrib import admin
from django.urls import path, include
from finders import views

urlpatterns = [
    path('', include('finders.urls')),
    path('admin/', admin.site.urls),
]