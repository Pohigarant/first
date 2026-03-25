from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets

from .models import Category, Product, Buyer, Review
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .serializers import CategorySerializer, ProductSerializer, BuyerSerializer, ReviewSerializer


def hello_view(request):
    return JsonResponse(
        {
            "message": "Hello World!",
            "status": "success",
        }
    )

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer