from django.contrib import admin
from .models import Courses,Lecture, Department

admin.site.register(Courses)
admin.site.register(Lecture)
admin.site.register(Department)
