from django.urls import path
from . import views 

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('cat1/', views.Categorya1, name='cat1'),
    path('cat2/', views.Categorya2, name='cat2'),
    path('cat3/', views.Categorya3, name='cat3'),
    path('cantact/', views.Contact, name='contact'),
    path("single/", views.Single, name="single"),
    path('author/', views.Author, name='author'),
]
