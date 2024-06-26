from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home_page'),
    path('architects_list', views.architects_list, name='architects_list'),
    path('add_architect', views.add_architect, name='add_architect'),

]


