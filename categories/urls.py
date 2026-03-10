
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name="hello_view"),
    path('category/', views.CategoryCreateView.as_view(), name="category"),

    path('category/<int:cat_id>', views.CategoryDetailView.as_view(), name="category_view"),

]