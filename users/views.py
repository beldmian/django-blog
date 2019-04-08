from django.shortcuts import render, redirect
from .forms import UserRegistration
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form =  UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are registred successful by name {username}, enter valid username and password for login into your account')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request,'users/registration.html',{'form': form, 'title': 'Registration'})

def profile(request):
    return render(request, 'users/profile.html', {'title': 'Profile'})