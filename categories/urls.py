
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import CategoryViewSet
router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='cat')

urlpatterns = [

    path('', include(router.urls)),


]