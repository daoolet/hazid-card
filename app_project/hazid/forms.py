from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import CustomUser, Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = [field.name for field in Survey._meta.get_fields() if field.name not in ("created_at", "author")]
        widgets = {
            # "activity_observed": forms.CheckboxSelectMultiple,
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

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