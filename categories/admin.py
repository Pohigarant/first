from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from slugify import slugify

from .models import Product, Category, Buyer, Review, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'quantity', 'is_active',"product_info",
                    'created_at', 'updated_at', "category"]
    list_display_links = ['id', 'name']
    ordering = ['name', 'created_at']
    prepopulated_fields = {'slug': (slugify('name'),)}
    list_editable = ['is_active','price','product_info']
    list_per_page = 20
    list_filter = ['price', 'quantity', 'is_active', 'created_at', "category_id"]
    search_fields = ['name', 'slug', 'article']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug': (slugify('name'),)}
    ordering = ['name']
    list_editable = ['name']
    list_per_page = 20
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Buyer)
class BuyerAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone','city', 'is_staff', 'birth_date')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone','birth_date')}),
    )
    # Добавляем наши поля в форму создания нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'birth_date')}),
    )


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id','quantity','created_at','user']
    ordering = ['quantity']
    list_editable = ['quantity']
    list_per_page = 20
    list_filter = ['quantity']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating','text','created_at','product__name','user__email']
    ordering = ['rating']

    list_per_page = 20
    search_fields = ['rating']
    list_filter = ['rating']
