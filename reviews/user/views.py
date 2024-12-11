from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .form import *
from django.contrib import messages
# Create your views here.

def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(request)
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'User not found or invalid details')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        if form.is_valid():
            form.save()
            return redirect('my_account')  # Redirect to a success page
        else:
            print(form)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def my_account(request):
    pass

def custom_logout(request):
    logout(request)
    return redirect('home')

def contact(request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                # Send email
                send_mail(
                    f"{subject.capitalize()} - {subject}",  # Subject includes chosen option
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
        else:
            form = ContactForm()
        return render(request, 'contact.html', {'form': form})
