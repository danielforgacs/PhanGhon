from django import forms
from . import models




class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = models.User
        fields = (
            'username',
            'password',
        )
        widgets = {
            'password': forms.PasswordInput(),
        }
