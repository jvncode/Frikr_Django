from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC
from django.urls import reverse

def home(request):
    """
    Esta función devuelve el home de mi pagina
    """
    photos = Photo.objects.filter(visibility=PUBLIC, owner='1').order_by('-created_at') #Con order_by hacemos que ordene la consulta con la fecha de creacion
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

def detail(request, pk):
    """
    Carga la página de detalle de una foto
    :param request: HttpRequest
    :param pk: id de la foto
    :return: HttpResponse
    """
    """
    También podemos utilizar esta sintaxis de recuperación de un objeto:
    try:
        photo = Photo.objects.get(pk=pk)
    except Photo.DoesNotExist:
        photo = None
    except PhotoMultipleObjects:
        photo = None
    """
    possible_photos = Photo.objects.filter(pk=pk)
    photo = possible_photos[0] if len(possible_photos) >= 1 else None
    if photo is not None:
        #cargar la pagina de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto')  # 404 Not found

def create(request):
    """
    Muestra un formulario para crear una foto y la crea si la petición es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ''
    if request.method == 'GET':
        form = PhotoForm()
    else:
        form = PhotoForm(request.POST)
        if form.is_valid():
            new_photo = form.save()  # Guarda el objeto Photo y me lo devuelve
            form = PhotoForm()
            success_message = 'Guardado con éxito!'
            success_message += '<a href="{}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += 'Ver foto'
            success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message
    }
    return render(request, 'photos/new_photo.html', context)