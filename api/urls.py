from django.urls import path
from . import views



urlpatterns = [
    path('read/', views.PostApi.as_view(), name='read-api'),
    path('add/', views.CreatPostApi.as_view(), name='add-api'),
    path('universal/<int:pk>/', views.Unversal.as_view(), name="universal"),
    path('delete/<int:pk>/', views.DeleteCategorya.as_view(), name='apidelete'),
    path('update/<int:pk>/', views.UpdateCategorya.as_view(), name='apiupdate'),
]
