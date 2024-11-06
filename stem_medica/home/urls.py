from django.urls import path
from django.contrib.auth.views import LoginView
from .views import contact_us, about_us

urlpatterns = [
    path('contact-us/', contact_us, name='contact-us-page'),
    path('about-us/', about_us, name='about-us-page'),
]
