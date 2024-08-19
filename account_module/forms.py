from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from account_module.models import Factors

User = get_user_model()
class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(),label="تکرار رمز عبور",
                                       error_messages={'required':'تکرار رمز عبور اجباری میباشد'})
    class Meta:
        model = User
        fields = ['phone', 'password']

        widgets = {
            'phone': forms.TextInput(),
            'password': forms.PasswordInput(),
        }
        labels = {
            'phone': 'شماره همراه:',
            'password': "رمز عبور:",
        }
        error_messages = {
            'phone': {
                'required': 'شماره همراه اجباری می باشد. لطفا وارد کنید'
            },
            'password':{
                'required':'رمز عبور اجباری میباشد لطفا آن را وارد کنید'
            }

        }
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone']

        widgets = {
            'phone': forms.TextInput(attrs={'placeholder':'مانند:09139071847'}),

        }
        labels = {
            'phone': 'شماره همراه:',

        }
        error_messages = {
            'phone': {
                'required': 'شماره همراه اجباری می باشد. لطفا وارد کنید'
            },


        }

class EditProfileForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['full_name', 'address']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی:',
            'address': "آدرس:",
        }


class UserCreationFormNoPassword(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone', 'full_name', 'address', 'melli_code', 'code_posty')

    def save(self, commit=True):
        user = super().save(commit=False)
        # If you need to set any default values or process data, do it here
        if commit:
            user.save()
        return user