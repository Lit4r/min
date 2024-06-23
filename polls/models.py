from django.db import models
from django.conf import settings

class Lecture(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Лекция')
    content_lecture = models.TextField(max_length=1800, verbose_name='Текст')
    course_id = models.ForeignKey('polls.Courses', on_delete=models.CASCADE, null=True, related_name='lecture', verbose_name='Название курса')
    
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Название курса')
    department_id = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, related_name='courses', verbose_name='Профессия')

    def __str__(self):
        return self.title

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name='Профессия')
    students = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.title