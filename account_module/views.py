from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
import base64
from django.views.generic import View
from .forms import  RegisterForm, LoginPasswordForm
from django.contrib.auth import get_user_model, login, logout
from django_otp.plugins.otp_totp.models import TOTPDevice
import pyotp
from .utils.sms_package import SMSHandler
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

class RegisterView(View):
    def get(self, request):

        register_form = RegisterForm()
        context = {'register_form': register_form,
                    'error': 'false'
                   }

        return render(request, 'account_module/register_form.html' , context)

    def post(self, request):
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():

            user_password = register_form.cleaned_data['password']
            phone_number = request.session.get('phone_number', None)

            user = User.objects.filter(phone=phone_number).first()

            if user is not None:
                user.set_password(user_password)
                user.is_active = True
                user.save()
                login(request, user)
                # otp_value = send_otp(user)
                # request.session['otp_value'] = otp_value
                # request.session['phone_number'] = phone_number
                #
                #
                #
                # sms_object = SMSHandler(user.phone, otp_value)
                # try:
                #     # sending sms
                #     status = SMSHandler.send_otp(sms_object)  # status of sending sms
                #
                #     # send alert and return to login page if status is False
                #     if status == True:
                #         return HttpResponseRedirect(f"{reverse('verify')}?alert=true")
                #     else:
                #         return HttpResponseRedirect(f"{reverse('verify')}?alert=false")
                # except Exception:
                #     return HttpResponseRedirect(f"{reverse('login')}?alert=error")
                return redirect('my_account')



            else:
                return HttpResponseRedirect(f"{reverse('login')}?alert=error")
        else:
            context = {
                'register_form': register_form,
                'error': 'true'
            }
            return render(request, 'account_module/register_form.html', context)


class LoginView(View):
    def get(self, request):

        return render(request, 'account_module/login.html')

    def post(self, request: HttpRequest):

        user_phone = request.POST.get('phone')

        user, created = User.objects.get_or_create(phone=user_phone)

        if not created:
            if (user.password == ''):
                request.session['phone_number'] = user_phone
                return HttpResponseRedirect(f"{reverse('register')}?alert=true")

            otp_value = send_otp(user)


            # set object of sms class
            sms_object = SMSHandler(user.phone, otp_value)

            request.session['otp_value'] = otp_value
            request.session['phone_number'] = user_phone

            # try to send sms to user
            try:
                status = SMSHandler.send_otp(sms_object)  # status of sending sms

                # send alert and return to login page if status is False
                if status == True:
                    return HttpResponseRedirect(f"{reverse('verify')}?alert=true")
                else:
                    return HttpResponseRedirect(f"{reverse('verify')}?alert=false")
            except Exception:
                return HttpResponseRedirect(f"{reverse('login')}?alert=error")

        elif(user.password == ''):
            request.session['phone_number'] = user_phone
            return redirect('register')

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




    # set object of sms class
    sms_object = SMSHandler(user.phone, otp_value)

    request.session['otp_value'] = otp_value
    request.session['phone_number'] = user_phone

    # try to send sms to user
    try:
        status = SMSHandler.send_otp(sms_object)  # status of sending sms

        # send alert and return to login page if status is False
        if status == True:
            return HttpResponseRedirect(f"{reverse('verify')}?alert=true")
        else:
            return HttpResponseRedirect(f"{reverse('verify')}?alert=false")
    except Exception:
        return HttpResponseRedirect(f"{reverse('login')}?alert=error")



class LoginPasswordView(View):
    def get(self, request):
        login_password_form = LoginPasswordForm()
        context = {
            'login_password_form': login_password_form
        }
        return render(request, 'account_module/login_password.html', context)
    def post(self, request):
        login_password_form = LoginPasswordForm(request.POST)
        if login_password_form.is_valid():
            user_phone = request.session['phone_number']
            user = User.objects.get(phone=user_phone)
            if user :
                if user.check_password(request.POST['password']):
                    login(request, user)
                    return redirect('my_account')
                else:
                    login_password_form.add_error('password', 'کلمه عبور اشتباه است.')

        context = {
            'login_password_form': login_password_form
        }
        return render(request, 'account_module/login_password.html', context)

def LogoutView(request):
    logout(request)
    return redirect('home-page')