from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.imported_product_list, name='imported_product_list'),
]
