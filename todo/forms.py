from django import forms
from .models import Todo

class AddForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('task',)