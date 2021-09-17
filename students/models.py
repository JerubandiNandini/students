from django.db import models


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    rollnumber = models.AutoField(primary_key=True)
    college = models.ForeignKey(College, related_name='mark', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name


class Mark(models.Model):
    student = models.ForeignKey(Student, related_name='mark', on_delete=models.DO_NOTHING)
    subject_name = models.CharField(max_length=200)
    mark = models.IntegerField(max_length=200)

    def __int__(self):
        return self.student

class Subject(models.Model):
    rollnumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    sub1 = models.IntegerField(max_length=200)
    sub2 = models.IntegerField(max_length=200)
    sub3 = models.IntegerField(max_length=200)
    sub4 = models.IntegerField(max_length=200)

    def __int__(self):
        return self.rollnumber