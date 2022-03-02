import imp
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from . models import Userpassword

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            Userpassword(username=username, password=password1).save()
            messages.success(request, f'Account has been created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

    
