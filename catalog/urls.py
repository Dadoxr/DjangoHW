import os, sys
sys.path.append(os.getcwd())

from django.urls import path
from catalog.views import ContactCreateView, ProductDetialView, ProductListView, ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    # path('', products, name='products'),
    # path('contacts/', contact, name='contacts'),
    # path('product/', product),
    # path('add_product/', add_product, name='add_product'),
    
    path('', ProductListView.as_view(), name='products'),
    path('contacts/', ContactCreateView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetialView.as_view(), name='product'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),

]
