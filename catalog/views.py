import os, sys
sys.path.append(os.getcwd())

from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from catalog.models import Contact, Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, CreateView, ListView


## FBV-метод
# def products(request):
# 	all_products = Product.objects.all() 
# 	paginator = Paginator(all_products, 3)  
# 	page = request.GET.get('page')

# 	try:
# 		products = paginator.page(page)
# 	except PageNotAnInteger:
# 		products = paginator.page(1)
# 	except EmptyPage:
# 		products = paginator.page(paginator.num_pages)
# 	context = {'object_list': products,} 
# 	return render(request, 'catalog/products.html', context)


## CBV-метод
class ProductListView(ListView):
	model = Product
	paginate_by = 3



## FBV-метод
# def contact(request):
# 	if request.method == 'POST':
# 		name = request.POST.get('name')
# 		phone = request.POST.get('phone')
# 		message = request.POST.get('message')
# 		Contact.objects.create(name=name, phone=phone, message=message)
# 	return render(request, 'catalog/contact.html')

## CBV-метод
class ContactCreateView(CreateView):
	model = Contact
	fields = ('name', 'phone', 'message', )
	success_url = reverse_lazy('catalog:products')



## FBV-метод
# def product(request):
# 	first_object = Product.objects.all().first()
# 	context = {'object': first_object}

# 	return render(request, 'catalog/product.html', context)

## CBV-метод
class ProductDetialView(DetailView):
	model = Product

	def get_queryset(self, *args, **kwargs):
		queryset = super().get_queryset(*args, **kwargs)
		queryset = queryset.filter(pk=self.kwargs.get('pk'))

		return queryset



## FBV-метод
# def add_product(request):
# 	categories = Category.objects.all()
# 	context = {'object_list': categories}
# 	if request.method == 'POST':
# 		name = request.POST.get('name')
# 		description = request.POST.get('description')
# 		preview = request.FILES['preview']
# 		category_name = request.POST.get('category')
# 		category = Category.objects.get(name=category_name)
# 		price = request.POST.get('price')

# 		Product.objects.create(name=name, description=description, preview=preview, category=category, price=price)
# 	return render(request, 'catalog/add_product.html', context)


## CBV-метод
class ProductCreateView(CreateView):
	model = Product
	fields = ('name', 'description', 'preview', 'category', 'price')
	success_url = reverse_lazy('catalog:products')
