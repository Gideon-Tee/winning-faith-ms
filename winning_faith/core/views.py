from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Classroom, Teacher, Fee
from .forms import EnrollStudentForm, ClassroomForm, TeacherForm
from django.db.models import Q

# Create your views here.



@login_required(login_url='login')
def index(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    classrooms = Classroom.objects.all()
    jhs_students = Student.objects.filter(classroom='jhs')
    # for student in jhs1_students:
    #     student.fees_paid -= 700.00 
    context = {
        'students': students,
        'jhs_students': jhs_students,
        'student_population': len(students),
        'teacher_population': len(teachers),
        'num_of_classes': len(classrooms)
    }
    return render(request, 'index.html', context)



@login_required(login_url='login')
def student_fees(request):
    classrooms = Classroom.objects.all()
    students = Student.objects.all()
    students_owing_fees = Student.objects.filter(is_owing=True).order_by('lname', 'fname')
    # for student in students_owing_fees:
    #     print(student.fees_rem)
    context = {
        'classrooms': classrooms,
        'students': students,
        'students_owing': students_owing_fees
    }
    return render(request, 'student_fees.html', context)



@login_required(login_url='login')
def finance(request):
    Fee.crech = 500.00
    Fee.lower_primary = 540.00
    Fee.upper_primary = 650.00
    Fee.jhs = 750.00

    students = Student.objects.all()
    fees = [Fee.crech, Fee.lower_primary, Fee.upper_primary, Fee.jhs]

    context = {
        'fees': fees,
        'students': students,
        'fee_crech': Fee.crech,
        'fee_lower_primary': Fee.lower_primary,
        'fee_upper_primary': Fee.upper_primary,
        'fee_jhs': Fee.jhs
    }

    return render(request, 'finance.html', context)



@login_required(login_url='login')
def display_students(request):
    try:
        search = request.GET.get('search_student')
        if search:
            
            students = Student.objects.filter(
                Q(full_name__icontains=search)
            ).order_by('lname', 'fname')
        else:
            students = Student.objects.all().order_by('lname', 'fname')
    except Exception as e:
        print(f'error:: {e}')
        messages.error(request, 'An error occurred')
        return redirect('index')
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
    students = Student.objects.all()
    for classroom in classes:
        classroom.num_of_students = 0
        for student in students:
            if student.classroom == classroom:
                classroom.num_of_students += 1
            

    context = {
        'classes': classes
    }
    return render(request, 'all_classes.html', context)



@login_required(login_url='login')
def add_new_class(request):
    form = ClassroomForm()


    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Class created successfully')
            return redirect('classes')
        
            
    
    return render(request, 'add_new_class.html', {'form': form})



@login_required(login_url='login')
def add_teacher(request):
    form = TeacherForm()
    classrooms = Classroom.objects.all()

    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers')

    context = {
        'classrooms': classrooms,
        'form': form
    }

    return render(request, 'add_teacher.html', context)
    


@login_required(login_url='login')
def enroll(request):
    classes = Classroom.objects.all()
    form = EnrollStudentForm()
    
    if request.method == 'POST':
        form = EnrollStudentForm(request.POST)
        if form.is_valid():
            classroom = form.cleaned_data['classroom']
            classroom = Classroom.objects.get(name=classroom)
            classroom.num_of_students += 1
            classroom.save()
            form.save()
        return redirect('students')
    
    context = {'classes': classes, 'form': form}

    
    return render(request, 'enroll.html', context)



def student(request, id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        print('student id not found')
        messages.error(request, 'id not found in database')
        return redirect('students')
    
    context = {'student': student}
    return render(request, 'student-details.html', context)


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