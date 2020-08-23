from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accountcrud.forms import LoginForm
from django.contrib import messages


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create(username=data['username'])
            user.set_password(data['password1']) # cannot be set as password
            user.save()
            return redirect('/accounts/login')
    form = UserCreationForm()
    context_var = {'form':form}
    return render(request,'signup.html',context_var)



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(request,username=username,password=password)
            print(user)
            if user is not None: # if authenticated
                login(request,user)
                return redirect('/read_student')
            else:
                messages.warning(request,'Login Error! Username or Password incorrect')
                return redirect('/accounts/login')

    form = LoginForm()
    context_var = {'form':form}
    return render (request,'login.html',context_var)


def logout_user(request):
    logout(request)
    return redirect('/')
