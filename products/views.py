from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from products.models import Product
from django.db.models import Q
from products.forms import ProductForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.




class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'



    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(price__icontains=search_query) |
                Q(quantity__icontains=search_query)
                )
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_products = Product.objects.all()

        context['all_products'] = len(all_products)

        little_stock_product_list = []

        for product in all_products:
            if product.quantity <= 10 or product.quantity == 1:
                little_stock_product_list.append(product)

        total_little_stock_product = len(little_stock_product_list)

        context['total_little_stock_product'] = total_little_stock_product

        without_stock_products = []

        for product in all_products:
            if product.quantity <= 0:
                without_stock_products.append(product)

        total_without_stock_products = len(without_stock_products)

        context['total_without_stock_products'] = total_without_stock_products


        return context


class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:Products')

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.name = self.request.POST.get('name')
            form.instance.description = self.request.POST.get('description')
            form.instance.price = self.request.POST.get('price')
            form.instance.quantity = self.request.POST.get('quantity')
        return super().form_valid(form)
    


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:Products')

    def form_valid(self, form):
        form.instance.name = form.instance.name
        return super().form_valid(form)
    


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('products:Products')