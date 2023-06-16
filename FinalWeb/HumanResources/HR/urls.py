from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('add/', views.add, name='add'),
    path('addVF/<int:EmployeeID>/', views.addVF, name='addVF'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:EmployeeID>', views.delete, name='delete'),
    path('VR/approve/<name>', views.approve, name='approve'),
    path('VR/reject/<name>', views.reject, name='rejcet'),
    path('update/<int:EmployeeID>', views.update, name='update'),
    path('update/updaterecord/<int:EmployeeID>', views.updaterecord, name='updaterecord'),
    path('searchEmployee/',views.searchEmployee,name = 'searchEmployee'),
    path('getEmployee/',views.getEmployee, name = 'getEmployee'),
    path('VR/',views.VRDisplay,name='VRDisplay'),
    # path('VR/',views.vacationRequest,name='vr'),
    path('outPut/',views.outPut, name = 'outPut'),
    path('getEmployee/vacationForm.html/', views.addVF, name='addVF'),
    path('getEmployee/addVF/<int:EmployeeID>', views.addVF, name='addVF'),
    path('vacationForm.html/<int:EmployeeID>/', views.addVF, name='addVF'),
    path('getEmployee/addVF/addVacationForm/<int:EmployeeID>', views.addVacationForm, name='addvacationForm'),

 


    # path('update/', views.update, name='update'),
    # path('updateEmp/', views.updateEmp, name='updateEmp'),
    # # path('delete/<event_id>', views.delete, name='delete'),
    # path('getEmployee/vacationFormFields/<int:EmployeeID>', views.vacationFormFields, name='vacationFormFields'),
    # path('getEmployee/vacationFormFields/fillVacationFormFields/<int:EmployeeID>', views.fillVacationFormFields, name='fillVacationFormFields'),
]

