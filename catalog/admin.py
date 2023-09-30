from django.contrib import admin
import os, sys
sys.path.append(os.getcwd())

from catalog.models import Category, Product

@admin.register(Category)
class UnivercityAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)
	
	
@admin.register(Product)
class UnivercityAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price', 'category')
	list_filter = ('category',)
	search_fields = ('name', 'description',)
	