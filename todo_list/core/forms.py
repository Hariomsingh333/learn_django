from django.forms import ModelForm
from .models import Todo_data


class Todo_Form(ModelForm):
    
    class Meta:
        model = Todo_data
        fields = ("__all__")
