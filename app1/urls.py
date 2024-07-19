from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('home/', views.home, name='home'),
    path('test1/', views.test1, name='test1'),
]
