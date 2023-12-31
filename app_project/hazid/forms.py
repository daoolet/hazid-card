from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User


from .models import CustomUser, Survey, AllowedUser


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [field.name for field in Survey._meta.get_fields() if field.name not in ("created_at", "author")]


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={"class": "form-input"})
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-input"})
    )


class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        model = CustomUser


class AllowedUserForm(forms.ModelForm):
    class Meta:
        model = AllowedUser
        fields = ('email',)