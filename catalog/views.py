import os, sys
sys.path.append(os.getcwd())

from config import settings
from django.shortcuts import render
from catalog.models import Contact, Product

def home(request):
	last_two = Product.objects.all().order_by('-id')[:2]
	print(last_two)

	return render(request, 'catalog/home.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		Contact.objects.create(name=name, phone=phone, message=message)
	return render(request, 'catalog/contact.html')
