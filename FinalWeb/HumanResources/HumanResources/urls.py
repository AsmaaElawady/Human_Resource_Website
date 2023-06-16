"""
URL configuration for HumanResources project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from HR import views

urlpatterns = [
    path('', include('HR.urls')),
    path('', views.HomePage, name='HomePage'),
    path('update/',include('HR.urls')),
    # path('updateEmp/',include('HR.urls')),
    path('admin/', admin.site.urls),
    path('phase1',views.phase1,name='phase1'),
    path('HomePage',views.HomePage,name='HomePage'),
    path('addVF/<int:EmployeeID>/',views.addVF,name='addVF'),
    path('table',views.table,name='table'),
]


