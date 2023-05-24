from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:EmployeeID>', views.delete, name='delete'),
    path('update/<int:EmployeeID>', views.update, name='update'),
    path('update/updaterecord/<int:EmployeeID>', views.updaterecord, name='updaterecord'),
    path('searchEmployee/',views.searchEmployee,name = 'searchEmployee'),
    path('getEmployee/',views.getEmployee, name = 'getEmployee'),
    path('VR/',views.VRDisplay,name='VRDisplay'),
    path('outPut/',views.outPut, name = 'outPut'),
    # path('getEmployee/vacationForm.html', views.VFDisplay, name = 'VFL'),
    # path('update/', views.update, name='update'),
    # path('updateEmp/', views.updateEmp, name='updateEmp'),
    # # path('delete/<event_id>', views.delete, name='delete'),
    path('vacationFormFields/<int:EmployeeID>', views.vacationFormFields, name='vacationFormFields'),
    path('vacationFormFields/fillVacationFormFields/<int:EmployeeID>', views.fillVacationFormFields, name='fillVacationFormFields'),
]

