import os, sys
sys.path.append(os.getcwd())

from config import settings
from django.shortcuts import render


def home(request):
	return render(request, 'catalog/home.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		with open(settings.FORM_DATA_PATH, 'a') as f:
			f.write(f'name={name}, phone={phone}, message={message}\n\n')
	return render(request, 'catalog/contact.html')
