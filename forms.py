from django import forms
from django.contrib.auth.models import User
from .models import Loan 
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
   
    
class LoanApplicationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['amount', 'tenure',]