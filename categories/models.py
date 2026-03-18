from django.contrib.auth.models import User, AbstractUser
from django.db import models
from slugify import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        # Если slug не передан (пустая строка) — генерируем из name
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='products',
                                 verbose_name="Категория",
                                 null=True, blank=True)

    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="URL слаг")
    article = models.CharField(max_length=50, verbose_name="Артикул", blank=True)
    product_info = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество товара")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if self.pk:
            old = Product.objects.get(pk=self.pk)
            if old.name != self.name:
                self.slug = slugify(self.name)
        else:
            if not self.slug:
                self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})


class Buyer(AbstractUser):
    city = models.CharField(max_length=100, blank=True, verbose_name="Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    email = models.EmailField(max_length=255, unique=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=30, blank=True, verbose_name="Номер мобильного телефона")




class Basket(models.Model):
    user = models.OneToOneField(Buyer, on_delete=models.CASCADE,
                                null=True, blank=True, related_name="basket",
                                verbose_name="Покупатель")

    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Review(models.Model):
    product = models.ForeignKey(
        Product,
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

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.user.name}"
