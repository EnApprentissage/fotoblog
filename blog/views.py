from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms,models

@login_required
def upload_photo(request):
    form = forms.PhotoForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect('home')
    return render(request, 'blog/upload_photo.html', {'form': form})


@login_required
def home(request):
    photos = models.Photo.objects.all()
    return render(request, 'blog/home.html', context={'photos': photos})