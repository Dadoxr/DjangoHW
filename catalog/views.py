import os, sys
sys.path.append(os.getcwd())

from config import settings
from django.shortcuts import render
from catalog.models import Category, Contact, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def home(request):
	all_products = Product.objects.all() 
	paginator = Paginator(all_products, 3)  
	page = request.GET.get('page')

	try:
		products = paginator.page(page)
	except PageNotAnInteger:
		products = paginator.page(1)
	except EmptyPage:
		products = paginator.page(paginator.num_pages)
	context = {'object_list': products,} 
	return render(request, 'catalog/home.html', context)


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		Contact.objects.create(name=name, phone=phone, message=message)
	return render(request, 'catalog/contact.html')

def product(request):
	first_object = Product.objects.all().first()
	context = {'object': first_object}

	return render(request, 'catalog/product.html', context)

def add_product(request):
	categories = Category.objects.all()
	context = {'object_list': categories}
	if request.method == 'POST':
		name = request.POST.get('name')
		description = request.POST.get('description')
		preview = request.FILES['preview']
		category_name = request.POST.get('category')
		category = Category.objects.get(name=category_name)
		price = request.POST.get('price')

		Product.objects.create(name=name, description=description, preview=preview, category=category, price=price)
	return render(request, 'catalog/add_product.html', context)
