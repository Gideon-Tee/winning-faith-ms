from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Classroom, Teacher

# Create your views here.

students = Student.objects.all()


@login_required(login_url='login')
def index(request):
    jhs_students = Student.objects.filter(category='jhs')
    # for student in jhs1_students:
    #     student.fees_paid -= 700.00 
    context = {
        'students': students,
        'jhs_students': jhs_students,
        'student_population': len(students)
    }
    return render(request, 'index.html', context)



@login_required(login_url='login')
def display_students(request):
    students = Student.objects.all().order_by('fname', 'lname')
    context = {
        'students': students
    }
    return render(request, 'student_info.html', context)

@login_required(login_url='login')
def display_teachers(request):
    teachers = Teacher.objects.all().order_by('fname', 'lname')
    context = {
        'teachers': teachers
    }
    return render(request, 'display_teachers.html', context)


@login_required(login_url='login')
def display_classes(request):
    classes = Classroom.objects.all()
    for classroom in classes:
        for student in students:
            if student.classroom == classroom.name:
                classroom.num_of_students += 1
            

    context = {
        'classes': classes
    }
    return render(request, 'all_classes.html', context)



@login_required(login_url='login')
def add_new_class(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        class_teacher = request.POST['class_teacher']

        new_class = Classroom.objects.create(
            name = name,
            class_teacher = class_teacher,
            category = category
        )
        new_class.save()
        messages.info(request, 'Class created successfully')
        return redirect('classes')
    else:
        return render(request, 'add_new_class.html')

@login_required(login_url='login')
def add_teacher(request):
    classrooms = Classroom.objects.all()
    context = {
        'classrooms': classrooms
    }
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        other_names = request.POST['other_names']
        assigned_class = request.POST['assigned_class']

        classroom = Classroom.objects.get(name = assigned_class)

        new_teacher = Teacher.objects.create(
            fname = fname,
            lname = lname,
            other_names = other_names,
            assigned_class = classroom
        )
        new_teacher.save()
        messages.info(request, 'new teacher added successfully')
        return redirect('teachers')
    
    else:
        return render(request, 'add_teacher.html', context)


@login_required(login_url='login')
def enroll(request):
    classes = Classroom.objects.all()
    context = {'classes': classes}

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
        return render(request, 'enroll.html', context)


def settings(request):

    return render(request, 'settings.html')

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