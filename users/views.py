from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        # if this is a post request, pass the data to the form.
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # this saves all the form data for us
            form.save()
            username = form.cleaned_data.get('username')
            # flash messages are for one time messages. becomes part of the request
            messages.success(request, f'Account created! You are now able to login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        # can give the forms the same data types to autofill information
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # since the profile update is going to have files in the req, must pass that to the form as well.
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

        messages.success(request, f'Account updated.')
        return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'users/profile.html', context)