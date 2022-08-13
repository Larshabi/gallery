from rest_framework import serializers
from .models import Category, Seller, Product

class CategorySerializer(serializers.ModelSerializer):
    random_photo = serializers.SerializerMethodField()
    
    def get_random_photo(self, obj):
        try:
            return obj.products.first().photo
        except:
            return""
        
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'random_photo'
        ]
        
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = [
            'id',
            'name'
        ]
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'photo',
            'asin',
            'price',
            'title',
            'category',
            'seller'
        ]
        
class ProductAllofaSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()
    class Meta:
        model = Product 
        fields = [
            'id',
            'photo',
            'asin',
            'price',
            'title',
            'category',
            'seller'
        ]
    def create(self, validated_data):
        categories = validated_data.pop('category')
        cat = dict(categories)
        category=Category.objects.create(name=cat["name"])
        sellers = validated_data.pop('seller')
        sel = dict(sellers)
        seller=Seller.objects.create(name=sel["name"])
        photo = validated_data['photo']
        asin = validated_data['asin']
        price = validated_data['price']
        title= validated_data['title']
        product = Product.objects.create(category=category, seller=seller, photo=photo, asin=asin, price=price, title=title)
        return product