from django.contrib import admin
from app02 import models
from .models import Grade,Student,Teacher
# Register your models here.
class StundetAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender','birth','grade',)
admin.site.register(Student,StundetAdmin)
# class GradeAdmin(admin.ModelAdmin):
#     list_display = ('grade','teacher',)

admin.site.register(models.Teacher)
admin.site.register(models.Grade)