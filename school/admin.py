from django.contrib import admin
from .models import Student, Teacher


class TeacherInline(admin.TabularInline):
    model = Student.teachers.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
