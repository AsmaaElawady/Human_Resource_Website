from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import RegisterForm 
from .models import RegisteredVacationForm
from django.shortcuts import render
from django.views.decorators.csrf  import csrf_exempt


def vacationRequest(request):
  from django.core import serializers
  data = serializers.serialize("python", RegisteredVacationForm.objects.all())
  
  context = {
    'data' : data
  }

  return render(HttpResponse, 'VR.html', context)


def index(request):
  return render(request, 'homePage.html')
  

def add(request):
  template = loader.get_template('phase1.html')
  return HttpResponse(template.render({}, request))


def addrecord(request):
  EmployeeID = request.POST['EmployeeID']
  EmployeeName = request.POST['EmployeeName']
  email = request.POST['email']
  phone = request.POST['phone']
  Addres = request.POST['Addres']
  Salary = request.POST['Salary']
  NumberVacation = request.POST['NumberVacation']
  NumberApprovedVacation = request.POST['NumberApprovedVacation']
  Date = request.POST['Date']
  Gender = request.POST['Gender']
  Status = request.POST['Status']
  MARITALSTATUE = request.POST['MARITALSTATUE']

  member = RegisterForm(EmployeeID=EmployeeID,EmployeeName=EmployeeName,email=email,phone=phone,Addres=Addres,Salary=Salary,NumberVacation=NumberVacation,NumberApprovedVacation=NumberApprovedVacation,Date=Date,Gender=Gender,Status=Status,MARITALSTATUE=MARITALSTATUE )
  member.save()
  return HttpResponseRedirect(reverse('phase1'))


def delete(request, EmployeeID):
  member = RegisterForm.objects.get(EmployeeID=EmployeeID)

  member.delete()
  return HttpResponseRedirect(reverse('HomePage'))


def update(request, EmployeeID):
  mymember = RegisterForm.objects.get(EmployeeID=EmployeeID)
  template = loader.get_template('editinfo.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def vacationFormFields(request, EmployeeID):
  mymember = RegisterForm.objects.get(EmployeeID=EmployeeID)
  template = loader.get_template('searchEmpOutput.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def approve(request, name, id):
  num1 = RegisterForm.objects.filter(EmployeeID=id)
  n1 = num1[0].NumberVacation
  n2 = num1[0].NumberApprovedVacation

  num2 = RegisteredVacationForm.objects.filter(VFID=id)
  n3 = num2[0].VFFromDate
  n4 = num2[0].VFToDate

  n5 = n4 - n3
  RegisterForm.objects.filter(EmployeeName=name).update(NumberVacation = n1 - n5.days - 1)
  RegisterForm.objects.filter(EmployeeName=name).update(NumberApprovedVacation = n2 + n5.days + 1)

  vacationForm = RegisteredVacationForm.objects.get(VFName=name)
  vacationForm.delete()
  return HttpResponseRedirect(reverse('HomePage'))



def reject(request, id):
  vacationForm = RegisteredVacationForm.objects.filter(VFID=id)
  vacationForm[0].delete()
  return HttpResponseRedirect(reverse('HomePage'))

def updaterecord(request, EmployeeID):
  EmployeeName = request.POST['EmployeeName']
  EmployeeID = request.POST['EmployeeID']
  email = request.POST['email']
  phone = request.POST['phone']
  Addres = request.POST['Addres']
  Salary = request.POST['Salary']
  NumberVacation = request.POST['NumberVacation']
  NumberApprovedVacation = request.POST['NumberApprovedVacation']
  member = RegisterForm.objects.get(EmployeeID=EmployeeID)
  member.EmployeeName = EmployeeName
  member.EmployeeID = EmployeeID
  member.email = email
  member.phone = phone
  member.Addres = Addres
  member.Salary = Salary
  member.NumberVacation = NumberVacation
  member.NumberApprovedVacation = NumberApprovedVacation
  member.save()
  return HttpResponseRedirect(reverse('table'))


def fillVacationFormFields(request, EmployeeID):
  EmployeeName = request.POST['EmployeeName']
  EmployeeID = request.POST['EmployeeID']
  member = RegisterForm.objects.get(EmployeeID=EmployeeID)
  member.EmployeeName = EmployeeName
  member.EmployeeID = EmployeeID
  member.save()
  return HttpResponseRedirect(reverse('HomePage'))

def phase1(request):
  return render(request, 'phase1.html')


def table(request):
  mymembers = RegisterForm.objects.all().values()
  template = loader.get_template('table.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def HomePage(request):
  return render(request, 'HomePage.html')


def home(request):
  return render(request, 'home.html')


def VRDisplay(request):
    from django.core import serializers
    data = serializers.serialize("python", RegisteredVacationForm.objects.all())

    context = {
      'data' : data
    }

    return render(request, 'VR.html', context)


def addVF(request,EmployeeID):
  mymember = RegisterForm.objects.get(EmployeeID=EmployeeID)
  template = loader.get_template('vacationForm.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def searchEmployee(request):
  return render(request,'searchEmp.html')


@csrf_exempt
def getEmployee(request):
    name = request.POST['empName']
    employees = RegisterForm.objects.filter(EmployeeName__icontains = name)
    results_html = {}
    for employee in employees:
      results_html[employee.EmployeeName] = employee.EmployeeID

    context = {"results":results_html}

    return render(request,'searchEmpOutput.html',context)


def outPut(request):
  return render(request,"searchEmpOutput.html")


def addVacationForm(request,EmployeeID):
  VFName = request.POST.get('VFName')
  VFID = request.POST.get('VFID')
  VFFromDate = request.POST.get('VFFromDate')
  VFToDate = request.POST.get('VFToDate')
  VFReason = request.POST.get('VFReason')
  VFStatus = request.POST.get('VFStatus')
  VFData = RegisteredVacationForm(VFName = VFName, VFID = VFID, VFFromDate = VFFromDate
                      , VFToDate = VFToDate, VFReason = VFReason, VFStatus = VFStatus)
  VFData.save()
  return HttpResponseRedirect(reverse('HomePage'))
