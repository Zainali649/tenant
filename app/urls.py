from django.urls import path

from .views import index, create_product

urlpatterns = [
    path('', index, name="product_index"),
    path('create_product', create_product, name="create_product")
]