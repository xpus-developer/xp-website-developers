from django.shortcuts import render, redirect
from .forms import ContactMessageForm
from .forms import ImageUploadForm
from .models import UploadedImage

def gallery(request):
    images = UploadedImage.objects.all()
    return render(request, 'gallery.html', {'images': images})

def index(request):
    
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('thank_you')  # Redirect to a thank you page after successful submission
    else:
        form = ContactMessageForm()

    return render(request, 'index.html', {'form': form})


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('thank_you')  # Redirect to a thank you page after successful submission
    else:
        form = ContactMessageForm()

    return render(request, 'contact.html', {'form': form})


def do(request):
    return render(request, 'do.html')

from django.shortcuts import render

def thank_you(request):
    return render(request, 'thank_you.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect to your gallery page
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})
