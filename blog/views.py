from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog
from pytils.translit import slugify

from blog.utils import send_mail_to_admin



class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog
    slug_field = 'slug' 

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        if self.object.views % 5 == 0:
            send_mail_to_admin(self.object)
        return self.object
    

class BlogCreateView(CreateView):
    model = Blog
    fields =('title', 'body', 'preview', 'is_active', )
    success_url = reverse_lazy('blog:list') 

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            if Blog.objects.filter(slug=new_article.slug).exists():
                new_article.slug = f'{new_article.slug}-{new_article.pk}'
            new_article.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields =('title', 'body', 'preview', 'is_active', )

    def get_success_url(self) -> str:
        return reverse('blog:article', args=[self.kwargs.get('slug')])
    

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


def change_is_active(request, slug):
    article = get_object_or_404(Blog, slug=slug)
    article.is_active = not article.is_active
    article.save()

    return redirect(reverse('blog:article', args=[slug]))