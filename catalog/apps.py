from django.apps import AppConfig
import os, sys
sys.path.append(os.getcwd())


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
