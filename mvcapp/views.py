from django.shortcuts import render
from mvcapp.models import Employee
#function madhe --> function based views.. --> every view function must have one default param--> which is request


def save_or_update_employee(request):
    message = ''
    if request.method == 'POST':
        formdata = request.POST     #request.form
        empid = formdata.get('eid')
        emp = Employee(name=formdata.get('ename'),
                       email=formdata.get('eemail'),
                       salary=formdata.get('esalary'),
                       city=formdata.get('ecity'),
                       state=formdata.get('estate'),
                       pincode=formdata.get('epincode'),
                       role=formdata.get('erole'))

        if empid:
            message = "Update Operation"
            emp.id = empid
        else:
            message = "Add Operation"

        emp.save()
        message = 'Emp saved Successfully...!'
    return render(request,'add_employee.html',{"result" : message})


def edit_employee(request,eid):
    empref = Employee.objects.get(id=eid)
    if empref:
        return render(request, 'add_employee.html', {"emprecord": empref})


def delete_employee(request,eid):
    empref = Employee.objects.get(id=eid)
    if empref:
        empref.delete()
    return render(request, 'list_employees.html', {'emplist': Employee.objects.all()})

def list_employees(request):
    return render(request,'list_employees.html',{'emplist' : Employee.objects.all()})

def welcome_page(request):
    return render(request,'index.html')
