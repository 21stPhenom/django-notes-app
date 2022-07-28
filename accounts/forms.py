from django import forms

class UserRegForm(forms.Form):
    first_name = forms.CharField(label="Enter first name")
    last_name = forms.CharField(label="Enter last name")
    username = forms.CharField(label="Enter username")
    email = forms.EmailField(label="Enter Email")
    password1 = forms.CharField(label="Enter password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label="Enter username")
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)