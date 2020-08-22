from django.shortcuts import render , redirect
from appcrud.forms import StudentsForm
from appcrud.models import Students
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# **************************** CRUD **********************************

# CREATE functionality:
@login_required
def add_student(request):
    if request.method == 'POST':
        forms = StudentsForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request,'Student has been registered successfully!')
            return redirect('/student')
        else:
            messages.warning(request,'Error during registration!')
            return redirect('/add_student')

    context_var = {'forms':StudentsForm()}
    return render(request,'add_student.html',context_var)


# READ Functionality:
@login_required
def read_student(request):
    student = Students.objects.all()
    context_var = {'student':student}
    return render(request,'read_student.html',context_var)



# UPDATE functionality:
@login_required # this decorator forces user to be logged in to update
def update_student(request,id):
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        forms = StudentsForm(request.POST)
        if forms.is_valid():
            forms.save()
            messages.success(request, 'Updated Successfully!')
            return redirect('/read_student')
        else:
            messages.warning(request, 'Error during Update!')
            return redirect('/update_student')

    context_var = {'forms': StudentsForm()}
    return render(request, 'update_student.html', context_var)



# DELETE functionality
@login_required
def delete_student(request,id):
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        messages.success(request,'Deleted Successfully!')
        return redirect('/read_student')




