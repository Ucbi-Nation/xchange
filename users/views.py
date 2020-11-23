from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


PAGINATION_COUNT = 10

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form2 = ProfileUpdateForm(request.POST)
        if form.is_valid() and form2.is_valid():
            form_save = form.save()
            address = form2.save(commit=False)
            address.user = form_save
            address.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            print(username)
            return redirect('signup')
    else:
        form = UserRegisterForm()
        form2 = ProfileUpdateForm()
    return render(request, 'users/signup.html', {'form': form,'form2':form2})


@login_required
def profile(request):
    if request.method == 'POST':
        uform = UserUpdateForm(request.POST, instance=request.user)
        pform = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if uform.is_valid() and pform.is_valid():
            uform.save()
            pform.save()
            messages.success(request, f'Account has been updated.')
            return redirect('profile')
    else:
        uform = UserUpdateForm(instance=request.user)
        pform = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'uform': uform, 'pform': pform})

