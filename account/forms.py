from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User



class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username"
            }
        )
    )
    password = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )


class SignUPForm(UserCreationForm):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Username"
            }
        )
    )
    first_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"First Name"
            }
        )
    )
    last_name = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Last Name"
            }
        )
    )
    password1 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password"
            }
        )
    )
    password2 = forms.CharField(
        widget= forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Re-Password"
            }
        )
    )
    email = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Example@gmail.com"
            }
        )
    )
    address = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"Address"
            }
        )
    )
    city = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"City"
            }
        )
    )
    state = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder":"State"
            }
        )
    )
    phone = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder":"Phone Number"
            }
        )
    )
    zip_code = forms.IntegerField(
        widget= forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder":"Zip Code"
            }
        )
    )
     

    class Meta:
        model = User
        fields = ('username','state','phone','address','city','zip_code','email','password1','first_name','last_name','password2')

    

class EditUserProfileForm(UserChangeForm):

    class Meta:
            model = User
            fields = ['first_name','state','last_name','phone','address','city','zip_code','profile_img']


class EditUserAddressForm(UserChangeForm):

    class Meta:
            model = User
            fields = ['first_name','last_name','phone','address','state','city','zip_code']




