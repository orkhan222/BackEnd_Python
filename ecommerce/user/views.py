from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from .forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')   
    context = {
        'form': form
    }
    return render(request,'register.html',context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index:index')
    return render(request,"login.html")

def logout(request):
    return redirect("login")