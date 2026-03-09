from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View

from categories.models import Category


def hello_view(request):
    return JsonResponse(
        {
            "message": "Hello World!",
            "status": "success",
        }
    )


def category(request):
    cats = Category.objects.all()
    return render(request, 'categories/category.html', {'cats': cats})


def about(request):
    return render(request, 'categories/about.html',status=200)


def category_view(request, cat_id):
    return HttpResponse(f'GET разрешён категория = {cat_id}')


