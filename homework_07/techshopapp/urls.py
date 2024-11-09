from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name="home"),
    path('items_create/', views.items_create, name="items_create"),
    # path('contacts/', views.contacts, name="contacts"),
    path('catalog/', views.catalog, name="catalog"),
]

