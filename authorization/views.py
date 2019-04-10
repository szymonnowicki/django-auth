from django.shortcuts import render

from django.views.generic import TemplateView

'''
    HOME AUTH PAGE
'''
class HomeAuthPage(TemplateView):
    template_name = 'home.html'


'''
    REGISTER
'''

class RegisterUser(TemplateView):
    template_name = 'register/register.html'