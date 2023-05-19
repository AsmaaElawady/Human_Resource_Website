from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('update/', views.update, name='update'),
    path('updateEmp/', views.updateEmp, name='updateEmp'),
]

