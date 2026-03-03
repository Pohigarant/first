from django.contrib import admin
from .models import Product, Category, Buyer, Review, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'quantity', 'is_active',"product_info",
                    'created_at', 'updated_at', "category"]
    list_display_links = ['id', 'name']
    ordering = ['name', 'created_at']
    list_editable = ['is_active','price','product_info']
    list_per_page = 20
    #list_filter = ['price', 'quantity', 'is_active', 'created_at', "category_id"]
    #search_fields = ['name', 'slug', 'article']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    ordering = ['name']
    list_editable = ['name']
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ['id','name','surname','email','city','phone','birth_date','registration_date']
    ordering = ['name','registration_date']
    list_editable = ['name','surname','email','city','phone','birth_date']
    list_per_page = 20


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ['id','quantity','created_at']
    ordering = ['quantity']
    list_editable = ['quantity']
    list_per_page = 20

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','rating','text','created_at']
    ordering = ['rating']
    list_editable = ['rating']
    list_per_page = 20