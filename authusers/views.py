from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegistrationForm  # Create this form in forms.py


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Replace 'home' with your project's home page
    else:
        form = UserRegistrationForm()
    return render(request, 'authusers/signup.html', {'form': form})


def login_view(request):
    # Your login logic here
    return render(request, 'authusers/login.html')

def signup_view(request):
    # Your signup logic here
    return render(request, 'authusers/signup.html')