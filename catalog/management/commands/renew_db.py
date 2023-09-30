import os,sys
sys.path.append(os.getcwd())
from django.core.management import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product

class Command(BaseCommand):
	
    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        call_command('loaddata', 'catalog_data.json')