
from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('create/', views.create, name="create"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),
]