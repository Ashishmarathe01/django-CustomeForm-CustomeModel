#form singup import
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Newuser
# athenticate import
from django.contrib.auth import authenticate

class RestrionForm(UserCreationForm):
    email=forms.EmailField(max_length=60,help_text='required.add a valid')

    class Meta:
        model=Newuser
        fields=('email','username','password1','phone','password2')


        # custimize autheicatio

class Authenticates(forms.ModelForm): # mention bco to hide password ####
    password=forms.CharField(label="password",widget=forms.PasswordInput)

    class Meta:
        model = Newuser
        fields = ('email',  'password' )

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("invalid login ")





