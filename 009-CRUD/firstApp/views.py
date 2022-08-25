from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "firstApp/index.html")

def student_list(request):
    students = Student.objects.all()
    context = {
        "students": students,
    }
    return render(request, "firstApp/student_list.html", context)
    # return render(request, "firstApp/student_list.html", {"students": students})

def student_add(request):
    form = StudentForm()
    if request.method=="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form
    }
    return render(request, "firstApp/student_add.html", context)

def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(instance=student)
    if request.method== "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")   
    context = {
        'form':form,
    }
    return render(request, 'firstApp/student_update.html', context)

def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method=="POST":
        student.delete()
        return redirect("list")
    return render(request, "firstApp/student_delete.html")

def student_detail(request, id):        
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    return render(request, 'firstApp/student_detail.html', context)

