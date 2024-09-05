from django import forms
from django.contrib.auth import get_user_model

from django.core.exceptions import ValidationError
import re

from langdetect import LangDetectException, detect


User = get_user_model()
class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'تکرار رمز عبور','id': 'confirm-password'}
        ),error_messages={'required':'تکرار رمز عبور اجباری میباشد'}
    )
    class Meta:
        model = User
        fields = ['password', 'confirm_password']

        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'رمز عبور','id' : 'new-password' , 'autocomplete': 'new-password'}),

        }
        labels = {

            'password': "رمز عبور:",
        }
        error_messages = {

            'password':{
                'required':'رمز عبور اجباری میباشد لطفا آن را وارد کنید'
            },
            'confirm_password':{
                'required': 'تکرار رمز عبور اجباری میباشد لطفا آن را وارد کنید'
            }

        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'رمز عبور با تکرار آن مطابقت ندارد')

class LoginPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'رمز عبور',
                'id': 'password',
                'autocomplete': 'password'
            }
        ),
        label="رمز عبور:",
        error_messages={
            'required': 'رمز عبور اجباری میباشد لطفا آن را وارد کنید'
        }
    )
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
        fields = ['full_name', 'address', 'melli_code', 'code_posty']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'melli_code': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'code_posty': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'rows': 5,
                'id': 'message'
            })
        }
        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری می باشد. لطفا وارد کنید'
            },
            'address': {
                'required': 'آدرس اجباری می باشد. لطفا وارد کنید'
            },
            'melli_code': {
                'required': 'کد ملی اجباری میباشد لطفا آن را وارد کنید'
            },
            'code_posty': {
                'required': 'کد پستی اجباری میباشد لطفا آن را وارد کنید'
            }

        }

        labels = {
            'full_name': 'نام و نام خانوادگی:',
            'address': "آدرس کامل:",
            'melli_code': 'کد ملی:',
            'code_posty': 'کد پستی بدون خط فاصله (مانند: 0123456789):'
        }

    from langdetect import detect
    from langdetect.lang_detect_exception import LangDetectException

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        try:
            detected_lang = detect(full_name)
            print(detected_lang)
            if detected_lang != 'fa' and detected_lang != 'ar' and detected_lang != 'ur':
                raise ValidationError('نام و نام خانوادگی باید به فارسی وارد شود.')
        except LangDetectException:
            raise ValidationError('نام و نام خانوادگی باید به فارسی وارد شود.')
        return full_name

    def clean_address(self):
        address = self.cleaned_data.get('address')
        try:
            detected_lang = detect(address)
            print(detected_lang)

            if detected_lang != 'fa' and  detected_lang != 'ar' and  detected_lang != 'ur':
                raise ValidationError('آدرس باید به فارسی وارد شود.')
        except LangDetectException:
            raise ValidationError('آدرس باید به فارسی وارد شود.')
        return address




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