from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='nhome'),
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:EmployeeID>', views.delete, name='delete'),
    path('update/<int:EmployeeID>', views.update, name='update'),
    path('update/updaterecord/<int:EmployeeID>', views.updaterecord, name='updaterecord'),
    
    
    
    
    # salmaa
    path('searchEmployee/',views.searchEmployee,name = 'searchEmployee'),
    path('updateEmployee/', views.updateEmployee, name = 'updateEmployee'),

    # path('update/', views.update, name='update'),
    # path('updateEmp/', views.updateEmp, name='updateEmp'),
    # # path('delete/<event_id>', views.delete, name='delete'),
]

