from .models import *
import django_filters

class LectureFilter(django_filters.FilterSet):
    class Meta: 
        model = Lecture
        fields = ('course_id', 'title', 'content_lecture')