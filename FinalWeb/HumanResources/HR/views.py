from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import RegisterForm 
from .models import VacationForm
# from .models import Upform 
from django.shortcuts import render
from django.views.decorators.csrf  import csrf_exempt
# from .models import Upform

def index(request):
  return render(request, 'HomePage.html')
  
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
  return HttpResponseRedirect(reverse('index'))


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
  return HttpResponseRedirect(reverse('index'))

def fillVacationFormFields(request, EmployeeID):
  EmployeeName = request.POST['EmployeeName']
  EmployeeID = request.POST['EmployeeID']
  member = RegisterForm.objects.get(EmployeeID=EmployeeID)
  member.EmployeeName = EmployeeName
  member.EmployeeID = EmployeeID
  member.save()
  return HttpResponseRedirect(reverse('index'))

def phase1(request):
  return render(request, 'phase1.html')


def table(request):
  mymembers = RegisterForm.objects.all().values()
  # template = loader.get_template('phase1.html')
  template = loader.get_template('table.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def HomePage(request):
  return render(request, 'HomePage.html')

def VRDisplay(request):
    employees = VacationForm.objects.values('VFName')
    return render(request, 'VR.html', {'employees': employees})    

def VFDisplay(request):
    # template = loader.get_template('vacationForm.html')
    # return HttpResponse(template.render({}, request))
    return render(request,'vacationForm.html')

def addVF(request):
  template = loader.get_template('vacationForm.html')
  return HttpResponse(template.render({}, request))

def searchEmployee(request):
  return render(request,'searchEmp.html')

@csrf_exempt
def getEmployee(request):

    name = request.POST['empName']

    employees = RegisterForm.objects.filter(EmployeeName__icontains = name)
    # results_html = []
    #
    #
    # for employee in employees:
    #   results_html.append(employee.EmployeeName +" "+ employee.EmployeeID)
    results_html = {}
    for employee in employees:
      results_html[employee.EmployeeName] = employee.EmployeeID


    context = {"results":results_html}

    return render(request,'searchEmpOutput.html',context)


def outPut(request):
  return render(request,"searchEmpOutput.html")


def addVacationForm(request):
  VFName = request.POST.get('VFName')
  ID = request.POST.get('VFID')
  VFFromDate = request.POST('VFFromDate')
  VFToDate = request.POST.get('VFToDate')
  VFReason = request.POST.get('VFReason')
  VFStatus = request.POST.get('VFStatus')
  VFData = VacationForm(VFName = VFName, VFID = ID, VFFromDate = VFFromDate
                      , VFToDate = VFToDate, VFReason = VFReason, VFStatus = VFStatus)
  VFData.save()
  return HttpResponseRedirect(reverse('VFDisplay'))

# def VF(request):
#   return render(request, 'vacationForm.html')

# #function to render the update page
# def update(request):
#     mymembers = RegisterForm.objects.all().values()
#     template = loader.get_template('update.html')
#     context = {
#       'mymembers': mymembers,
#     }
#     return HttpResponse(template.render(context, request))
#   #  template = loader.get_template('update.html')
#   #  return HttpResponse(template.render({}, request))

# def updateEmp(request ):
#     template = loader.get_template('editinfo.html')
#     return HttpResponse(template.render({}, request))

#   #template = loader.get_template('editinfo.html')
#   #return HttpResponse(template.render({}, request))

# #function to get the values the user entered 
# #employee's data for which to update or delete




# # def delete(request, event_id):
# #     member = RegisterForm.objects.get(pk=event_id)
# #     member.delete()
# #     return HttpResponseRedirect(reverse('index'))

# def fillVacationFormFields(request, EmployeeID):
#   EmployeeName = request.POST['EmployeeName']
#   EmployeeID = request.POST['EmployeeID']
#   member = RegisterForm.objects.get(EmployeeID=EmployeeID)
#   member.EmployeeName = EmployeeName
#   member.EmployeeID = EmployeeID
#   member.save()
#   return HttpResponseRedirect(reverse('index'))

# def vacationFormFields(request, EmployeeID):
#   mymember = RegisterForm.objects.get(EmployeeID=EmployeeID)
#   template = loader.get_template('searchEmpOutput.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))



# def home(request):
#   if 1==1:
#     name=request.POST.get('EmployeeName')
#     return HttpResponse(name)
#   return render(request, 'phase1.html',{'mysorm':RegisterForm})


#     # return render(request, 'home.html')

