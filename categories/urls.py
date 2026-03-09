
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name="hello_view"),
    path('category/', views.category, name="category"),
path('about/', views.about, name="about"),
    path('category/<int:cat_id>', views.category_view, name="category_view"),
    path('category/<slug:slug_id>', views.category_view_slug, name="category_view_slug"),
]