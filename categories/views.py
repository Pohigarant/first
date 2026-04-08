from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Category, Product, Buyer, Review
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .permissions import IsOwnerOrReadOnly,  IsOwnerOrAdmin
from .serializers import CategorySerializer, ProductSerializer, BuyerSerializer, ReviewSerializer, RegisterSerializer


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


class BuyerRegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'user': {'id': user.id, 'username': user.username, 'email': user.email},
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            },
            status=status.HTTP_201_CREATED,
        )
