from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import RegisterForm

'''
    HOME AUTH PAGE
'''
class HomeAuthPage(TemplateView, FormView):
    template_name = 'home.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super(HomeAuthPage, self).get_context_data(**kwargs)
        context["form"] = self.form_class
        return context

def register_check(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    if request.method == 'POST':
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        return redirect('succes_register')

class SuccesRegister(TemplateView):
    template_name = 'register/succes_register.html'