from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from django.db import models

from apps.accounts.forms import AuthenticationForm, RegistrationForm

class Login(View):
    form = AuthenticationForm
    def get(self, request):
        print request
        form = self.form(None, request.POST)
        context = {'form' : form}
        return render(request, 'accounts/login.html', context)
    def post(self, request):
        print request
        form = self.form(request.POST)
        context ={'form': form}
        print "***********"
        print form
        print form['email']
        print form['password']
        if form.is_valid():
            print "Valid@@@@@@@@@@"
            email = form.cleaned_data['email']
            print email
            password = form.cleaned_data['password']
            print password
            user = authenticate(email=email, password=password)
            print user
            if user is not None:
                login(request, user)
                return redirect('/pokes/')
            else:
                return render(request, 'accounts/login.html', context)
        else:
            return render(request, 'accounts/login.html', context)

class Register(View):
    form = RegistrationForm
    def get(self, request):
        context = {'form' : self.form()}
        print context
        return render(request, 'accounts/register.html', context)
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            print "save new user"
            form.save()
            return redirect('/main/')
        else:
            context = {'form' : form}
            return render(request,'accounts/register.html', context)

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/main/')

