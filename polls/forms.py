from django import forms
from .models import Courses, Lecture
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = (NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class LectureForm(forms.ModelForm):

    class Meta:
        model = Lecture
        fields = ('title', 'content_lecture', 'course_id',)

class CoursesForm(forms.ModelForm):
    
    class Meta:
        model = Courses
        fields = ('title','department_id')