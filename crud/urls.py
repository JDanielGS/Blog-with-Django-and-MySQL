from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('write/', views.write, name="write"),
    path('insert/', views.insert, name="insert"),
    path('post/<int:id>', views.post, name="post"),
]
