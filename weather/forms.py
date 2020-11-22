from . models import City
from django.forms import ModelForm, TextInput

class cityForm(ModelForm):
    class Meta():
        model = City
        fields = ['name']
        widgets = {'name': TextInput(
            attrs={
                'class':'find-city',
                'name': 'city',
                'id': 'city',
                'placeholder':'Enter city'
            }
        )}