from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from clients.models import Client
from django.db.models import Q
from clients.forms import ClientForm
from openpyxl import Workbook
from openpyxl.styles import Alignment, PatternFill, Font, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



#CLIENTS VIEWS
##############


class ClientList(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'


    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        if search_query:
            queryset = queryset.filter(
                Q(fullname__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(address__icontains=search_query)
                )
        return queryset
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        all_clients = Client.objects.all()
        context['all_clients'] = len(all_clients)

        return context

        





class AddClient(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'add_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients:Clients')

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.instance.fullname = self.request.POST.get('fullname')
            form.instance.email = self.request.POST.get('email')
            form.instance.phone = self.request.POST.get('phone')
            form.instance.address = self.request.POST.get('address')
        return super().form_valid(form)
    

class UpdateClient(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'update_client.html'
    form_class = ClientForm
    success_url = reverse_lazy('clients:Clients')

    def form_valid(self, form):
        form.instance.fullname = form.instance.fullname
        return super().form_valid(form)
    

class DeleteClient(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'delete_client.html'
    success_url = reverse_lazy('clients:Clients')


