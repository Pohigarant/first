from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import viewsets

from .models import Category
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

from .serializers import CategorySerializer


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
