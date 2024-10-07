from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_link, name='create_link'),
    path('links/', views.link_list, name='link_list'),
    path('<str:short_url>/', views.redirect_link, name='redirect_link'),
]
