from pyexpat import model
from django import forms
from .models import movie

class TaskForm(forms.ModelForm):
    class Meta:
        model = movie
        fields = '__all__'
