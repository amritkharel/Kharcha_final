from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import KharchaCreationForm
from .models import Kharcha

# Create your views here.
@login_required
def base(request):
    if request.method == 'POST':
        user = request.user
        form = KharchaCreationForm(request.POST)
        if form.is_valid():
            form.instance.user = user
            form.save()
            return redirect("base")
    else:
        form = KharchaCreationForm()
    return render(request, 'main/home.html', {"form": form})