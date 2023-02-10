from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','location','profile_img']