from django.urls import path, include
from clients.views import ClientList, AddClient, UpdateClient, DeleteClient

urlpatterns = [
    path('', ClientList.as_view(), name='Clients'),
    path('addclient/', AddClient.as_view(), name='AddClient'),
    path('updateclient/<int:pk>', UpdateClient.as_view(), name='UpdateClient'),
    path('deleteclient/<int:pk>', DeleteClient.as_view(), name='DeleteClient')
]