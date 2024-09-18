from django.forms import ModelForm
from .models import Creator
 
 
class CreateForm(ModelForm):
    class Meta:
        model = Creator
        fields = ('title', 'description', 'image',)
 
