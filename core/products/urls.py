from django.urls import path, include
from products.views import ProductList, AddProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', ProductList.as_view(), name="Products"),
    path('addproduct/', AddProduct.as_view(), name="AddProduct"),
    path('updateproduct/<int:pk>', UpdateProduct.as_view(), name="UpdateProduct"),
    path('deleteproduct/<int:pk>', DeleteProduct.as_view(), name="DeleteProduct"),
]