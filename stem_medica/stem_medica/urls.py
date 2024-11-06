from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('config/', admin.site.urls, name='admin-page'),
    path('', include('home.urls')),
    path('', include('users.urls'))
]
