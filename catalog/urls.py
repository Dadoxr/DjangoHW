import os, sys
sys.path.append(os.getcwd())

from django.urls import path
from catalog.views import add_product, contact, home, product


urlpatterns = [
    path('', home),
    path('contacts/', contact),
    path('product/', product),
    path('add_product/', add_product),
]
