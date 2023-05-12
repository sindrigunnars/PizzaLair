from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from userprofile.forms.profile_form import ProfileForm
from userprofile.models import UserProfile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    return render(request, 'userprofile/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = UserProfile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    return render(request, 'userprofile/profile.html', {
        'form': ProfileForm(instance=profile)
    })