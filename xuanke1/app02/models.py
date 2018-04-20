from django.db import models

# Create your models here.
class Student(models.Model):  #学生表
    name = models.CharField('姓名',max_length=20)
    age = models.IntegerField('年龄',default=20)
    gender = models.BooleanField()
    birth=models.DateTimeField('选课时间', auto_now_add=True, editable = True)
    grade = models.ForeignKey("Grade")
    def __str__(self):
        return self.name

class Teacher(models.Model):  #老师表
    name=models.CharField('老师姓名',max_length=20)
    def __str__(self):
        return self.name


class Grade(models.Model):  #班级表
    grade=models.CharField('班级',max_length=20)
    teacher=models.ManyToManyField("Teacher")
    def __str__(self):
        return self.grade

# class Course(models.Model):  #课程表
#     name=models.CharField(max_length=30,name='课程名字',null=False)
#     teach=models.ForeignKey("Teacher")
#     def __str__(self):
#         return self.course_name