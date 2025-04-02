from django.urls import path
from blog import views

urlpatterns = [
    path('', views.hello, name="hello"), #URL de prueba
    path('list_articles/', views.list_articles, name="list_articles")
]