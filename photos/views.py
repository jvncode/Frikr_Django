from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

def home(request):
    photos = Photo.objects.all().order_by('-created_at') #Con order_by hacemos que ordene la consulta con la fecha de creacion
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)
