from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdateView, change_is_active

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('article/<slug>', BlogDetailView.as_view(), name='article'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<slug>', BlogUpdateView.as_view(), name='update'),
    path('delete/<slug>', BlogDeleteView.as_view(), name='delete'),
    path('change_is_active/<slug>', change_is_active, name='change_is_active'), 
]