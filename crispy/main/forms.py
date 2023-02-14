from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import post_model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class post_form(forms.ModelForm):
    class Meta:
        model = post_model
        fields = ['title','description','is_private']


    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'