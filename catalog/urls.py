import os, sys
sys.path.append(os.getcwd())


from django.urls import path
from catalog.views import contact, home

urlpatterns = [
    path('', home),
    path('contacts/', contact),
]
