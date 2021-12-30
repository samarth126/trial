from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.db.models import fields
from chat.models import NewUser

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=NewUser
        fields=('email','user_name','first_name','about','password1','password2')


class UserLoginForm(forms.ModelForm):
    password=forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model=NewUser
        fields=('email', 'password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid credentials")