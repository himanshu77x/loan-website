from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import  LoanApplicationForm
from .models import Loan
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import LoanApplication


def home(request):
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def home(request):
    return HttpResponse("template path: home.html")

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['EMAIL']
        password = request.POST['password']

      
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use!')
        else:
            user = User(username=username, email=email, password=make_password(password))
            user.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('login')
    
    return render(request, 'register.html')
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('login_success')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
    


def apply_loan(request):
    if request.method == 'POST':
        form = LoanApplicationForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.user = request.user
            loan.save()
            return redirect('loan_success')  
    else:
        form = LoanApplicationForm()
    return render(request, 'apply_loan.html', {'form': form})


def loan_success(request):
    return render(request, 'loan_success.html')

from django.shortcuts import render

def login_success(request):
    return render(request, 'login_success.html')

def document(request):
    return render(request, 'document.html')


def loan_application(request):
    if request.method == "POST":
        title = request.POST.get('title')
        full_name = request.POST.get('full_name')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        loan_amount = request.POST.get('loan_amount')
        loan_purpose = request.POST.get('loan_purpose')
        address = request.POST.get('address')
        employment_status = request.POST.get('employment_status')

        LoanApplication.objects.create(
            title=title,
            full_name=full_name,
            date_of_birth=date_of_birth,
            email=email,
            phone_number=phone_number,
            loan_amount=loan_amount,
            loan_purpose=loan_purpose,
            address=address,
            employment_status=employment_status
        )

        return HttpResponse('Loan application submitted successfully!')

    return render(request, 'loan_application_form.html')




def terms(request):
    return render(request, 'terms.html')


def policy(request):
    return render(request, 'policy.html')




def personal(request):
    return render(request, 'personal.html')

def apna(request):
    return render(request, 'apna.html')


def eduction(request):
    return render(request, 'eduction.html')

def car(request):
    return render(request, 'car.html')


def nikl(request):
    return render(request, 'nikl.html')