from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone']

        widgets = {
            'phone': forms.TextInput()
        }
        labels = {
            'phone': 'شماره همراه:'
        }
        error_messages = {
            'phone': {
                'required': 'شماره همراه اجباری می باشد. لطفا وارد کنید'
            }
        }
