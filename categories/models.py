from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL слаг")

    class Meta:
        db_table = 'Категории'
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='products',
                                 verbose_name= "Категория",
                                 null=True, blank=True)

    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL слаг")
    article = models.CharField(max_length=50,verbose_name="Артикул", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество товара")
    is_active = models.BooleanField(default=True,verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Продукты'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Buyer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=30,unique=True)
    registration_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "Покупатели"
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Basket(models.Model):
    user = models.OneToOneField(Buyer, on_delete=models.CASCADE,
                                null=True, blank=True, related_name="basket",
                                verbose_name="Покупатель")

    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Продукты'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class Review(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='Отзывы',
        verbose_name="Товар"
    )
    user = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        verbose_name="Покупатель"
    )
    rating = models.PositiveSmallIntegerField(verbose_name="Оценка")  # например от 1 до 5
    text = models.TextField(verbose_name="Текст отзыва")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_name = "Отзывы"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


    def __str__(self):
        return f"Отзыв от {self.user.name}"