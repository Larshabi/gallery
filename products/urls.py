from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('categories/', CategoryView.as_view()),
    path('sellers/', SellerView.as_view()),
    path('product/', ProductListAPIView.as_view())
]
