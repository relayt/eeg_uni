from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from users.forms import UserLoginForm, UserRegistrationForm

def authorization(request):
    if request.method == 'POST':
        form1 = UserRegistrationForm(data=request.POST)
        form = UserLoginForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('application'))
        else:
            print(form1.errors)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('application'))
        else:
            print(form.errors)
            pass
    else:
        form = UserLoginForm()
        form1 = UserRegistrationForm()
    context = {'form': form, 'form1': form1}
    return render(request, 'users/authorization.html', context)
