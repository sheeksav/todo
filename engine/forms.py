from django import forms
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.contrib.auth import authenticate
from django.forms.util import ErrorList


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address not found')

        return email

    def clean_password(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email[:30].lower(), password=password)

            if not user:
                raise forms.ValidationError('Your email address and password could not be authenticated')

        return password


class SignUpForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    password = forms.CharField(max_length=200,
                               min_length=8,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'autocomplete': 'off'}),
                               help_text=u'Must be between 8 and 200 characters')

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Don't worry - we will convert to lower() before storage, I promise.
        if User.objects.filter(email=email.lower()).exists():
            raise forms.ValidationError(mark_safe('There is already an account associated with this email address. '
                                         'If you want, <a href="/login/">click here</a> to log in.'))

        return email


class AddTaskForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'type':'textarea',
            'placeholder':'Enter title here...',
            'class':'form-control',
        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'type':'text',
            'placeholder':'Enter description here...',
            'class':'form-control',
        }
    ))

