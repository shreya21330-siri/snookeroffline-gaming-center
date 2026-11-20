

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomerRegistrationForm


def home(request):
    return render(request, 'home.html')


def register_customer(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')

    else:
        form = CustomerRegistrationForm()

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


def customer_login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def customer_logout(request):
    if request.method == 'POST':
        logout(request)

    return redirect('home')
