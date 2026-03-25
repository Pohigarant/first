
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='cat')
router.register('product', ProductViewSet, basename='prod')

urlpatterns = [

    path('', include(router.urls)),


]