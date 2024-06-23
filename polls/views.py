from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as d_login
from django.contrib import messages
from .models import Courses, Department, Lecture
from .forms import UserRegisterForm, UserCreationForm, CoursesForm, LectureForm

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            d_login(request, user)
            return redirect('courses')
        else:
            messages.success(request, ("Ошибка, попробуйте снова..."))
            return redirect('/')
    
    return render(request, 'polls/login.html', {})

def post_list(request):
    return render(request, 'polls/post_list.html', {})

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'polls/courses.html', {'courses': courses})

def reg(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            d_login(request, user)
            messages.success(request, ("Регистрация прошла успешно!"))
            return redirect('courses')
    else:
        form = UserCreationForm()
    return render(request, "polls/registr.html", {'form': form })

def course_detail(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    lectures = Lecture.objects.filter(course_id=pk).order_by('course_id')
    return render(request, 'polls/course_detail.html', {'course': course, 'lectures': lectures})

def lecture_detail(request, pk):
    lectures = get_object_or_404(Lecture, pk=pk)
    return render(request, 'polls/lecture_detail.html', {'lectures': lectures})

def course_new(request):
    if request.method == "POST":
        form = CoursesForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CoursesForm()
    return render(request, 'polls/course_new.html', {'form': form})

def lecture_new(request):
    if request.method == "POST":
        form = LectureForm(request.POST)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = LectureForm()
    return render(request, 'polls/lecture_new.html', {'form': form})

def new(request):
    return render(request, 'polls/new.html')

def lecture_edit(request, pk):
    lectures = get_object_or_404(Lecture, pk=pk) 
    if request.method == "POST":
        form = LectureForm(request.POST, instance=lectures)
        if form.is_valid():
            lectures = form.save(commit=False)
            lectures.save()
            return redirect('lecture_detail', pk=lectures.pk)
    else:
        form = LectureForm(instance=lectures)
    return render(request, 'polls/lecture_edit.html', {'form': form})
