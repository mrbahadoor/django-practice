from django.shortcuts import render, get_object_or_404
from employees.models import Employee
from django.http import HttpResponse #,Http404

# Create your views here.
def employee_details(request, pk): #pk is primary key
    employee = get_object_or_404(Employee, pk=pk)

    context = {
        'employee' : employee,
    }

    return render(request, 'employee_detail.html', context)


    # try:
    #     employee = Employee.objects.get(pk=pk)
    #     print(employee)
    # except:
    #     raise Http404

