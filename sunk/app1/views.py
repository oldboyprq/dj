from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("a good man")


def num(request, num, num2):
    return HttpResponse("The num is %s and %s" % (num, num2))


from .models import Grades, Students


def grades(request):
    gradesList = Grades.objects.all()
    return render(request, 'app1/grades.html', {"grades": gradesList})


def students(request):
    studentsList = Students.objects.all()
    return render(request, 'app1/students.html', {"students": studentsList})


def gradesStudents(request, num):
    grade = Grades.objects.get(pk=num)
    studentsList = grade.students_set.all()
    return render(request, 'app1/students.html', {"students": studentsList})
