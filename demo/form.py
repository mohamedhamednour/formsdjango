from django import forms
from .models import Students,Foorm
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class Addstud(forms.ModelForm):

    class Meta:
        model = Students
        fields = ['name', 'age', 'track']

class Formss(forms.ModelForm):

    class Meta:
        model = Foorm
        fields = ['name', 'passw']


class Userauth(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

# class Forms(forms.ModelForm):
#     class Meta:
#         model = Foorm
#         fields = ['email', 'password1', 'password2']

# class SignUpForm(UserCreationForm):
#     email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
#
#     class Meta:
#         model=User
#         fields = {'username','email','password1','password2'}

    # id = models.AutoField(primary_key=True)
    # name=forms.CharField(max_length=200, required=True)
    # age=forms.IntegerField(max_length=200)
    # track=forms.CharField(max_length=100)

