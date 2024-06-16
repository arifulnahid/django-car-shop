from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .form import CustomerSignupForm, CustomerEditForm

# Create your views here.


def customer_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', {'form': form})


def customer_signup(request):
    form = CustomerSignupForm()
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html', {'form': form})


@login_required
def customer_profile(request):
    form = CustomerEditForm(instance=request.user)
    if request.method == 'POST':
        form = CustomerEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'profile.html', {'form': form})


def customer_logout(request):
    logout(request)
    return redirect('home')
