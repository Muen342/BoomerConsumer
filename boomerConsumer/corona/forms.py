from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')

# class InternProfileForm(forms.ModelForm):
#     class Meta:
#         model = InternProfile
#         fields = ('location', 'bio')
        
# class HRProfileForm(forms.ModelForm):
#     class Meta:
#         model = HRProfile
#         fields = ('company_name', 'website')

class UserForm(UserCreationForm):
    displayName = forms.DateField(help_text='Your Prefered Name')
    lastName = forms.CharField(help_text='Your Last Name')
    age = forms.IntegerField(help_text='age')
    email = forms.CharField(max_length=100, help_text='100 char limit')
    postalCode = forms.CharField(max_length=6, help_text='Postal Code no Spaces')
    phoneNumber = forms.CharField(help_text="input your phoneNumber")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'displayName', 'lastName', 'age', 'email', 'postalCode', 'phoneNumber' )