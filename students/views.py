from django.shortcuts import render
from django.views import View
from students.models import Student
from students.models import Subject

class Home(View):
    def get(self, request):
        all_students = Student.objects.all()
        context = {
            "all_students" : all_students
        }
        return render(request, 'home.html', context=context)


class Marksheet(View):
    def get(self, request, Name):
        student = Subject.objects.get(name=Name)
        print("here I am")
        total = student.sub1+student.sub2+student.sub3+student.sub4
        # for subject in marks:
        #     total = total + subject.mark
        context = {
            "total" : total,
            "average": total/4
        }
        return render(request, 'marks2.html', context=context)