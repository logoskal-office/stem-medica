from django.urls import path
from .views import publish_product, products_view, publish_category

urlpatterns = [
    path('publish/', publish_product, name='publish-product-page'),
    path('products/',products_view, name='products-page'),
    path('publish-category/', publish_category, name='publish-category-page'),
    
]
