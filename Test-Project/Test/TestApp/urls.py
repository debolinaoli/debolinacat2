# myapp/urls.py
from django.urls import path
from .views import home, login_view, about, contact, register

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
]
