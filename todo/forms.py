from django.forms import ModelForm
from .models import TaskItem

class TodoForm(ModelForm):
    class Meta:
        model = TaskItem
        fields = ['title', 'description', 'important']