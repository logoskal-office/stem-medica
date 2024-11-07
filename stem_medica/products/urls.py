from django.urls import path
from .views import publish_product, products_view

urlpatterns = [
    path('publish/', publish_product, name='publish-product-page'),
    path('products/',products_view, name='products-page'),
    
]
