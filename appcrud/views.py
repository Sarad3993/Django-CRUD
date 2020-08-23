from django.shortcuts import render , redirect
from appcrud.forms import StudentsForm
from appcrud.models import Students
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    student = Students.objects.all().count()
    context_var= {'student': student}
    return render(request,'base.html',context_var)

# **************************** CRUD operations **********************************

# CREATE functionality:
def add_student(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/read_student')
        else:
            messages.warning(request,'Error during registration!')
            return redirect('/add_student')

    context_var = {'form':StudentsForm()} 
    return render(request,'add_student.html',context_var)



# READ Functionality:
def read_student(request):
    student = Students.objects.all()
    context_var = {'student':student}
    return render(request,'read_student.html',context_var)



# UPDATE functionality:
@login_required # this decorator forces user to be logged in to update
def update_student(request,id):
    student= Students.objects.get(id=id) # here we must set variable as instance only
    if request.method == 'POST':
        form= StudentsForm(request.POST,instance=student) 
        if form.is_valid():
            form.save()
            return redirect('/read_student')
        else:
            messages.warning(request, 'Error during Update!')
            return redirect('/update_student')

    context_var = {'form':StudentsForm(instance=student)} 
    return render(request, 'update_student.html', context_var)



# DELETE functionality
@login_required
def delete_student(request,id):
    # stu_id = int(stu_id)
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        student.delete() 
        messages.success(request,'Deleted Successfully!')
        return redirect('/read_student')

    context_var = {'student':student}
    return render(request, 'delete_student.html',context_var)



