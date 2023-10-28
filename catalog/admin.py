from django.contrib import admin
import os, sys
sys.path.append(os.getcwd())

from catalog.models import Category, Product, Version

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)
	
	
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price', 'category')
	list_filter = ('category',)
	search_fields = ('name', 'description',)

@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
	list_display = ('id', 'product', 'name', 'version', 'is_active', )
	