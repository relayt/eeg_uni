from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Email or Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields.pop('password2')
