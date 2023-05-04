from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'userprofile/index.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('userprofile-index')
        else:
            print(form.errors)
    return render(request, 'userprofile/register.html', {
        'form': UserCreationForm()
    })
