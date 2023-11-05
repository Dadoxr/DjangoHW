import os, sys
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.forms import ValidationError
from django.http import Http404, HttpResponse

from catalog.services import get_all_products_from_cache_or_db
sys.path.append(os.getcwd())

from catalog.models import Contact, Product, Version

## CBV-метод
from django.urls import reverse, reverse_lazy
from catalog.forms import ProductForm, ProductStaffForm, VersionForm
from django.views.generic import DetailView, CreateView, ListView, UpdateView
from django.forms.models import BaseModelForm, inlineformset_factory



class ContactCreateView(CreateView):
	model = Contact
	fields = ('name', 'phone', 'message', )
	success_url = reverse_lazy('catalog:products')


class ProductListView(ListView):
    model = Product
    paginate_by = 8

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            if self.request.user.is_staff:
                context_data['object_list'] = get_all_products_from_cache_or_db()
            else:
                context_data['object_list'] = Product.objects.filter(owner=self.request.user)
        for product in context_data.get('object_list', []):
            active_version = product.version_set.filter(is_active=True).last()
            if active_version:
                product.active_version_number = active_version.version
                product.active_version_name = active_version.name
            else:
                product.active_version_number = "Нет версии"
                product.active_version_name = None
        return context_data
	


class ProductDetialView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'
    
    def get_object(self, *args, **kwargs):
        self.object = super().get_object(*args, **kwargs)
        if self.object.owner == self.request.user or self.request.user.is_staff:
            return self.object
        raise Http404
        

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset
    

class ProductCreateView(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'
    template_name = 'catalog/product_form_with_formset.html'

    def get_form_class(self):
        form_class = super().get_form_class()
        if self.request.user.is_staff and self.object.owner != self.request.user:
            form_class = ProductStaffForm
        return form_class

    def get_object(self, *args, **kwargs):
        self.object = super().get_object(*args, **kwargs)
        if self.object.owner == self.request.user or self.request.user.is_staff:
            return self.object
        raise Http404
    
    def get_success_url(self, *args, **kwargs):
        return reverse('catalog:update', args=[self.get_object().pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if not self.request.user.is_staff:
            SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
            if self.request.method == 'POST':
                context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
            else:
                context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
		# self.object = form.save() для создания

        if len([product.get('is_active') for product in formset.cleaned_data if product.get('is_active')]) > 1:
            raise ValidationError('Возможна лишь одна активная версия. Пожалуйста, активируйте только 1 версию.')

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)




## FBV-метод

# from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.shortcuts import render
# from django.urls import reverse

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


# def contact(request):
# 	if request.method == 'POST':
# 		name = request.POST.get('name')
# 		phone = request.POST.get('phone')
# 		message = request.POST.get('message')
# 		Contact.objects.create(name=name, phone=phone, message=message)
# 	return render(request, 'catalog/contact.html')


# def product(request):
# 	first_object = Product.objects.all().first()
# 	context = {'object': first_object}

# 	return render(request, 'catalog/product.html', context)


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


