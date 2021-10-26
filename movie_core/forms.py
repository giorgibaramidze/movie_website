from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('ასეთი მაილი უკვე არსებობს')
        return email




class CustomEmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email_id = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email_id, is_active=True).exists():
            messages.error(request, f"ასეთი მაილი არ არის დარეგისტრირებული")

        return email
