# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.db import transaction
# from .models import Customer, Manager,User
# class CustomerSignUpForm(UserCreationForm):
#     name=forms.CharField(required=True)
#     age=forms.CharField(required=True)
#     class Meta(UserCreationForm.Meta):
#         model = User
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
        
#         user.is_customer = True
#         user.save()
#         student = Customer.objects.create(user=user)
#         return user
# class ManagerSignUpForm(UserCreationForm):
#     name=forms.CharField(required=True)
#     age=forms.CharField(required=True)
  
#     class Meta(UserCreationForm.Meta):
#         model = User
 
#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
        
#         user.is_manager = True
#         user.save()
#         manager = Manager.objects.create(user=user)
        
#         manager.save()
 
#         return manager


from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer')