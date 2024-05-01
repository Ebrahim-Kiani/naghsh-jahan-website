from django.shortcuts import render
from django.views.generic import View
from .forms import RegisterForm
# Create your views here.

class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form':register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        pass
