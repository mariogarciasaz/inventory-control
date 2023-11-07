import datetime
from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from clients.models import Client
from products.models import Product
from clientsdata.models import ClientData
from collections import Counter
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages

# Create your views here.



class Login(LoginView):
    template_name = 'login.html'
    fields = ['username', 'password']
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('website:index')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.')
        return super().form_invalid(form)



class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = 'website:login'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        #CLIENTS DATA

        all_clients_list = Client.objects.all()

        total_clients = len(all_clients_list)

        context['total_clients'] = total_clients

    ###########################################################

        #PRODUCTS DATA

        all_products_list = Product.objects.all()

        total_products = len(all_products_list)

        context['total_products'] = total_products

    ###########################################################

        #CLIENTDATA DATA

        all_charged_list = ClientData.objects.all()

        total_charged_list = []

        for charged in all_charged_list:
            if charged.paid == True:
                total_charged_list.append(charged.total_deuda)

        total_charged = sum(total_charged_list)

        context['total_charged'] = total_charged

        context = self.little_stock_products(context)
        context = self.without_stock_products(context)
        context = self.sales_per_month(context)
        context = self.last_sales(context)
        

        return context
    
    def little_stock_products(self, context):

        all_products = Product.objects.all().order_by('quantity')

        little_stock_products_list = []

        for product in all_products:
            if product.quantity < 10 and product.quantity > 0:
                little_stock_products_list.append({
                    'name': product.name,
                    'quantity': product.quantity,
                })

        context['little_stock_products_list'] = little_stock_products_list[:5]

        return context
    

    def without_stock_products(self, context):

        all_products = Product.objects.all()

        without_stock_products_list = []

        for product in all_products:
            if product.quantity <= 0:
                without_stock_products_list.append({
                    'name': product.name,
                    'quantity': product.quantity,
                })
        
        context['without_stock_products_list'] = without_stock_products_list

        return context



    def sales_per_month(self, context):

        year = datetime.datetime.now().year
        all_sales = ClientData.objects.filter(start_date__year=year, paid=True)

        january = []
        february = []
        march = []
        april = []
        may = []
        june = []
        july = []
        august = []
        september = []
        october = []
        november = []
        december = []


        for sale in all_sales:
            if sale.start_date.month == 1:
                january.append(sale.total_deuda)
            elif sale.start_date.month == 2:
                february.append(sale.total_deuda)
            elif sale.start_date.month == 3:
                march.append(sale.total_deuda)
            elif sale.start_date.month == 4:
                april.append(sale.total_deuda)
            elif sale.start_date.month == 5:
                may.append(sale.total_deuda)
            elif sale.start_date.month == 6:
                june.append(sale.total_deuda)
            elif sale.start_date.month == 7:
                july.append(sale.total_deuda)
            elif sale.start_date.month == 8:
                august.append(sale.total_deuda)
            elif sale.start_date.month == 9:
                september.append(sale.total_deuda)
            elif sale.start_date.month == 10:
                october.append(sale.total_deuda)
            elif sale.start_date.month == 11:
                november.append(sale.total_deuda)
            elif sale.start_date.month == 12:
                december.append(sale.total_deuda)

        


        total_january = sum(january)
        total_february = sum(february)
        total_march = sum(march)
        total_april = sum(april)
        total_may = sum(may)
        total_june = sum(june)
        total_july = sum(july)
        total_august = sum(august)
        total_september = sum(september)
        total_october = sum(october)
        total_november = sum(november)
        total_december = sum(december)

        context['total_january'] = total_january
        context['total_february'] = total_february
        context['total_march'] = total_march
        context['total_april'] = total_april
        context['total_may'] = total_may
        context['total_june'] = total_june
        context['total_july'] = total_july
        context['total_august'] = total_august
        context['total_september'] = total_september
        context['total_october'] = total_october
        context['total_november'] = total_november
        context['total_december'] = total_december

        
        return context
    

    def last_sales(self, context):

        all_sales = ClientData.objects.all()

        last_sales = all_sales[:5]

        context['last_sales'] = last_sales

        return context
    




