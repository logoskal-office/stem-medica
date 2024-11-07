from django.urls import path
from .views import publish_product, search

urlpatterns = [
    path('publish/', publish_product, name='publish-product-page'),
    path('search/',search ),
    path('search/q=<str:query>', search)
    
]
