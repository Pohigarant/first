from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from .models import Category, Product, Buyer, Review
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .permissions import IsOwnerOrReadOnly,  IsOwnerOrAdmin
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

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [AllowAny()]
        return [IsAdminUser()]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            return [AllowAny()]
        return [IsAdminUser()]


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [IsOwnerOrAdmin, IsAuthenticated]


class BasketViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [IsOwnerOrAdmin]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
