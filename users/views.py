from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegisterForm, UpdateForm, UpdateProfileForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', { 'form': form })

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UpdateForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
    constext = { 'u_form': u_form, 'p_form': p_form }
    return render(request, 'users/profile.html', constext)

def logout(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'users/logout.html')