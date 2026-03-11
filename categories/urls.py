
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name="hello_view"),
    path('category/', views.CategoryView.as_view(), name="category"),
    path('category/create/', views.CategoryCreateView.as_view(), name="category_create"),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name="category_create"),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name="category_update"),



]