from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Category
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


def hello_view(request):
    return JsonResponse(
        {
            "message": "Hello World!",
            "status": "success",
        }
    )


class CategoryView(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = list(queryset.values())

        return JsonResponse(data, safe=False)


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        data = {'id': cat.id, 'name': cat.name, 'slug': cat.slug}
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'slug']
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Неверный JSON'}, status=400)

        form = self.get_form_class()(data)

        if form.is_valid():

            new_obj = form.save()

            return JsonResponse({
                'id': new_obj.id,
                'name': new_obj.name,
                'slug': new_obj.slug,
            }, status=201)  # 201 Created
        else:

            return JsonResponse(form.errors, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["id", 'name', 'slug']
    http_method_names = ['put', 'patch']

    def put(self, request, *args, **kwargs):
        return self._update(request, partial=False)

    def patch(self, request, *args, **kwargs):
        return self._update(request, partial=True)

        # def _update(self, request, partial):
        try:
            obj = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Категория не найдена'}, status=404)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Неверный JSON'}, status=400)

        form = self.get_form_class()(data, instance=obj, partial=partial)
        if form.is_valid():
            obj = form.save()
            return JsonResponse({
                'id': obj.id,
                'name': obj.name,
                'slug': obj.slug
            }, status=200)
        return JsonResponse(form.errors, status=400)

    def _update(self, request, partial):

        try:
            obj = self.get_object()
        except Http404:
            return JsonResponse({'error': 'Категория не найдена'}, status=404)


        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Неверный JSON'}, status=400)

        if partial:
            # 3. Частичное обновление (PATCH) – обновляем только переданные поля
            allowed_fields = set(self.fields)  # поля, разрешённые для обновления
            for field in data:
                if field in allowed_fields:
                    setattr(obj, field, data[field])
            try:
                obj.full_clean()  # проверяем уникальность и другие ограничения модели
                obj.save()
            except ValidationError as e:
                return JsonResponse(e.message_dict, status=400)
        else:
            # 4. Полное обновление (PUT) – используем форму для валидации
            form = self.get_form_class()(data, instance=obj)
            if form.is_valid():
                obj = form.save()
            else:
                return JsonResponse(form.errors, status=400)

        # 5. Успешный ответ
        return JsonResponse({
            'id': obj.id,
            'name': obj.name,
            'slug': obj.slug
        }, status=200)
