from django import forms
from django.contrib.auth.models import User
from users.models import UserProfileInfo


class UserForm(forms.ModelForm):  # base class
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):  # inherit from (forms.ModelsForm)

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
