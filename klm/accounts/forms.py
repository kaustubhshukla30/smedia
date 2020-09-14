from django import forms
from django.contrib.auth.models import User
from .models import profile

GENDERS = (
   ('male', 'MALE'),
   ('female', 'FEMALE'),
)

class UserForm(forms.ModelForm):
    username = forms.CharField(label = "Username")
    email = forms.EmailField(label = "Email")  #add validator for webmail id check
    password = forms.CharField(widget = forms.PasswordInput, label = "Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DetailsForm(forms.ModelForm):
    
    gender = forms.ChoiceField(choices=GENDERS, required=True)

    class Meta:
        model = profile
        fields = ['gender', 'dp']
