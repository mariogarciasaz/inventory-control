from django.urls import path, include
from website.views import Index, Login
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='website:login'), name='logout'),
]