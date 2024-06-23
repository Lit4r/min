from django.urls import path
from . import views

urlpatterns = [
path('post_list', views.post_list, name="post_list"),
path('', views.login, name="login"),
path('courses/', views.courses, name="courses"),
path('registration/', views.reg, name='reg'),
path('courses/<int:pk>/', views.course_detail, name='course_detail'),
path('courses/lecture/<int:pk>/', views.lecture_detail, name='lecture_detail'),
path('courses/new', views.course_new, name="course_new"),
path('lecture/new', views.lecture_new, name="lecture_new"),
path('new', views.new, name="new"),
path('lecture/<int:pk>/edit/', views.lecture_edit, name="lecture_edit"),
]