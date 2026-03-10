from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView
import json
from .models import Category


def hello_view(request):
    return JsonResponse(
        {
            "message": "Hello World!",
            "status": "success",
        }
    )


class CategoryView(ListView):
    model = Category

    def get(self,request,*args,**kwargs):
        queryset = self.get_queryset()
        data = list(queryset.values())

        return JsonResponse(data,safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self,request,*args,**kwargs):
        cat = self.get_object()
        data = {'id':cat.id,'name':cat.name, 'slug':cat.slug}
        return JsonResponse(data,safe=False)

class CategoryCreateView(CreateView):
    model = Category

    fields = ['name','slug']


    def post(self, request, *args, **kwargs):
        # 1. Парсим JSON
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Неверный JSON'}, status=400)

        # 2. Создаём форму с данными
        form = self.get_form_class()(data)

        # 3. Валидируем и сохраняем
        if form.is_valid():
            new_obj = form.save()
            # Формируем ответ с данными созданного объекта
            response_data = {
                'id': new_obj.id,
                'name': new_obj.name,
                'slug': new_obj.slug,
            }
            return JsonResponse(response_data, status=201)  # 201 Created
        else:
            # Возвращаем ошибки валидации
            return JsonResponse(form.errors, status=400)