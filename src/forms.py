from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout
from .models import *


User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)

        if username and password:
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active.")
        return super(UserLoginForm,self).clean()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username(choose an easy one!!)')
    name= forms.CharField(label='First name ')
    email = forms.EmailField(label='Email address',)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'name',
            'email',
            'password',
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email

class EventForm(forms.ModelForm):

    class Meta:
        model = event_registration
        # fields = ('name','email','contact','year','a','b','c','d','e')
        fields = ('name','email','contact','year')
        #labels = {'tech_quiz': 'Hackerrank','b': 'Django Workshop','c': 'Knockout Coding','d': 'Tech Quiz','e': 'Mock ICPC',}


class registerForm(forms.ModelForm):

    class Meta:
        model = registration
        # fields = ('name','email','contact','year','a','b','c','d','e')
        fields = ('name','email','roll_number','contact','year','a','b')
        #labels = {'tech_quiz': 'Hackerrank','b': 'Django Workshop','c': 'Knockout Coding','d': 'Tech Quiz','e': 'Mock ICPC',}

class ContactForm(forms.ModelForm):

    class Meta:
        model = contact_request
        fields = ('contact_name','contact_email','content')




class hkctForm(forms.ModelForm):
    class Meta:
        model = hkct_register
        fields = ('name','email','contact','year','a','b','c','d','e','f')

class hkctOutForm(forms.ModelForm):
    class Meta:
        model = hkct_ouside
        fields = ('name','email','contact','location','institute')