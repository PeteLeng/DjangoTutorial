from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def emp_list(request):
    employees = Employee.objects.all()
    context = {
        'employees': employees,
        }
    return render(request, 'core/list.html', context)

def emp_create(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp-list')

    context = {
        'form': form,
        }
    return render(request, 'core/create.html', context)

def emp_edit(request, pk):
    print(f"!!!!!!Request: {pk}")
    # Note the original url settings in the tutorial is wrong
    # See https://stackoverflow.com/a/32568100/17006775
    # Research regex url in doc
    emp = Employee.objects.get(pk=pk)
    form = EmployeeForm(instance=emp)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('emp-list')

    context = {
        'form': form,
        }

    return render(request, 'core/edit.html', context)

def emp_delete(request):
    return render(request, 'core/delete.html', context)
