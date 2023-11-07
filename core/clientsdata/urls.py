from django.urls import path, include
from clientsdata.views import DeleteClientData, ClientsDataList, AddClientData, UpdateClientData, generate_excel_report_client, generate_excel_report_allclients
from . import views

urlpatterns = [
    path('', ClientsDataList.as_view(), name='ClientsData'),
    path('clientdata/<int:pk>', views.client_data, name='ClientData'),
    path('addclientdata/<int:pk>', AddClientData.as_view(), name='AddClientData'),
    path('updateclientdata/<int:pk>', UpdateClientData.as_view(), name='UpdateClientData'),
    path('deleteclientdata/<int:pk>', DeleteClientData.as_view(), name='DeleteClientData'),
    path('report/<int:pk>', generate_excel_report_client, name='generate_report_client'),
    path('report', generate_excel_report_allclients, name='generate_excel_report_allclients')
]