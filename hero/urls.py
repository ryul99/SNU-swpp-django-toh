from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.id, name='id'),
    path('<str:name>/', views.name, name='name'),
]
