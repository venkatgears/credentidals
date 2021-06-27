from django import forms
from .models import register
class Userforms(forms.ModelForm):
    class Meta:   
        model =  register
        fields = [
            'name',
            'email',
            'password',
            'remember_this_credentials',
        ] 
        