from django.http import HttpRequest
from django.shortcuts import render, redirect
import base64
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login
from django_otp.plugins.otp_totp.models import TOTPDevice
import pyotp


# Create your views here.
User = get_user_model()

def send_otp(user):
    device, created = TOTPDevice.objects.get_or_create(user=user)
    if created:
        device.save()

    # Convert the binary key to a base32-encoded string
    base32_key = base64.b32encode(device.bin_key).decode('utf-8')

    # Generate the OTP using the base32-encoded key
    totp = pyotp.TOTP(base32_key)
    otp_value = totp.now()

    # Send the OTP value to the user's phone or email
    # Example: send_sms(user.phone_number, otp_value)

    return otp_value

    return otp_value

class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form':login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        context = {'login_form': login_form}

        user_phone = request.POST.get('phone')

        user, created = User.objects.get_or_create(phone=user_phone)

        otp_value = send_otp(user)
        print(otp_value)

        request.session['otp_value'] = otp_value
        request.session['phone_number'] = user_phone

        return redirect('verify')


class VerifyView(View):
    def get(self, request):
        return render(request, 'account_module/otp_form.html')
    def post(self, request):

        otp_value = request.POST['otp']

        phone_number = request.session['phone_number']
        user = User.objects.get(phone=phone_number)
        device = TOTPDevice.objects.get(user=user)


        if device.verify_token(otp_value):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('my_account')
        else:
            return render(request, 'account_module/otp_form.html', {'error': 'کد معتبر نمی باشد لطفا دوباره درخواست دهید'})


def resend_otp(request):

    user_phone = request.session['phone_number']

    user = User.objects.get(phone=user_phone)

    otp_value = send_otp(user)
    print(otp_value)

    request.session['otp_value'] = otp_value

    return redirect('verify')
