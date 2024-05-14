from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')



@login_required(login_url='login')
def enroll(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        other_names = request.POST['other_names']
        category = request.POST['category']
        classroom = request.POST['classroom']
        fees_paid = request.POST['fees_paid']
        date_enrolled = request.POST['date_enrolled']

        new_student = Student.objects.create(
            fname = fname,
            lname = lname,
            other_names = other_names,
            category = category,
            classroom = classroom,
            fees_paid = fees_paid,
            date_enrolled = date_enrolled
        )
        new_student.save()
        return redirect('index')
    else:
        return render(request, 'enroll.html')



def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')