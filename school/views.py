from django.shortcuts import render
from .models import Student


def students_list(request):
    context = {
        'students': Student.objects.all(). \
            prefetch_related('teachers'). \
            order_by('group')
    }
    return render(request, 'school/students_list.html', context)
