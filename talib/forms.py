from django import forms
from talib.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    passwod = forms.CharField(widget=forms.PasswordInput() )

    class Meta():
        model = User
        fields = ('last_name','first_name','username','email','passwod')
class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields =('country',)