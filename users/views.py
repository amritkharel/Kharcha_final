from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created successfully Please login now.")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form":form})
