from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.
def register(request):
    if request.method=='POST':
        # form=UserCreationForm(request.POST)
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created. You can now log in.')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    u_form=UserUpdateForm()
    p_form=ProfileUpdateForm()
    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)