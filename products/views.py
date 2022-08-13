from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializer import *
from .models import *

class ProductList(ListCreateAPIView):
    serializer_class = ProductAllofaSerializer
    queryset = Product.objects.all()
    
class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_fields = [
        'category__id'
    ]
    search_fields= [
        'title'
    ]
    
class CategoryView(ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class SellerView(ListCreateAPIView):
    serializer_class = SellerSerializer
    queryset = Seller.objects.all()
    