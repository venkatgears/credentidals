from django import forms
from .models import Register


class Userforms(forms.ModelForm):
    class Meta:
        model = Register
        fields = [
            "name",
            "email",
            "password",
            "remember_this_credentials",
        ]
