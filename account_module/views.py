from django.http import HttpRequest
from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model, login

# Create your views here.
User = get_user_model()
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form':register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        context = {
            'register_form': register_form
        }
        if register_form.is_valid():
            user_phone = register_form.cleaned_data['phone']
            user_password = register_form.cleaned_data['password']
            print(user_phone, user_password)
            user : bool = User.objects.filter(phone__iexact=user_phone).exists()
            if user == True:
                return register_form.add_error('phone', 'تلفن وارد شده وجود دارد')
            else:
                user = User(phone=user_phone, is_active=True)
                user.set_password(user_password)
                user.save()
                #return redirect('login')

        return render(request, 'account_module/register_page.html', context)

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
        user_password = request.POST.get('password')
        user = User.objects.filter(phone__iexact=user_phone).first()
        if user is not None:
            if user.check_password(user_password):
                print('login successful')
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('home-page'))
            else:
                login_form.add_error(None, 'Invalid password')
        else:
            login_form.add_error('phone', 'User with this phone does not exist')

        return render(request, 'account_module/login.html', context)


