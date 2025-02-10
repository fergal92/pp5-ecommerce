from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_list, name='view_list'),
    path('add/<item_id>/', views.add_to_list, name='add_to_list'),
    path('adjust/<item_id>/', views.adjust_list, name='adjust_list'),
    path('remove/<item_id>/', views.remove_from_list, name='remove_from_list'),
]