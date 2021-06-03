from django.forms import ModelForm

from .models import Todo

class TodoForm(ModelForm):
    class Meta:
      model = Todo
      #from will show us all fields in todo(exluding id field)
      fields = "__all__"