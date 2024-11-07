from django.urls import path
from django.contrib.auth.views import LoginView
from .views import contact_us, about_us, download, download_link

urlpatterns = [
    path('contact-us/', contact_us, name='contact-us-page'),
    path('about-us/', about_us, name='about-us-page'),
    path('download/', download, name='download'),
    path('download/<str:file_name>', download_link, name='download_link')
]
