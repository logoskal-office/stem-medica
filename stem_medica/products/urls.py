from django.urls import path
from .views import publish_product

urlpatterns = [
    path('publish/', publish_product, name='publish-product-page'),
    
]
