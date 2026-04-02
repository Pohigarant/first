from rest_framework import serializers

from categories.models import Category, Product, Buyer, Basket, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')
        read_only_fields = ['slug']

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Product
        fields = ["id", "name","model", "price", "quantity", "category"]
        read_only_fields = ["id", "created_at", "updated_at"]

class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = ["id", "first_name", "last_name", "email", "birth_date","email","phone","date_joined"]
        read_only_fields = ["id","date_joined"]
        extra_kwargs = {
            "password": {
                "write_only": True, }
        }


class BasketSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(slug_field='name', queryset=Product.objects.all())
    user = serializers.SlugRelatedField(slug_field='username', queryset=Buyer.objects.all())
    class Meta:
        model = Basket
        fields = ["id", "product", "user", "quantity", "created_at" ]
        read_only_fields = ["id", "created_at"]


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    product = serializers.SlugRelatedField(slug_field='name', read_only=True)
    class Meta:
        model = Review
        fields = ["id", "user", "rating", "product", "created_at"]
        read_only_fields = ["id", "created_at"]

