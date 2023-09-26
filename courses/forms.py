# forms.py
from django import forms
from .models import CreateCourse

class CourseForm(forms.ModelForm):
    class Meta:
        model = CreateCourse
        fields = ['title', 'code', 'description', 'year', 'semester']
