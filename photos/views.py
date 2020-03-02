from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from photos.forms import PhotoForm
from photos.models import Photo, PUBLIC
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator


class HomeView(View):  #Vista basada en una clase. Los GET y POST se definen en métodos/funciones.
    def get(self, request):
        """
        Este método devuelve el home de mi pagina
        """
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at') #Con order_by hacemos que ordene la consulta con la fecha de creacion
        context = {
            'photos_list': photos[:5]
        }
        return render(request, 'photos/home.html', context)

class DetailView(View):
    def get(self, request, pk):
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
        possible_photos = Photo.objects.filter(pk=pk).select_related('owner') #con 'select_related() añadimos al select de búsqueda en BBDD los campos que queremos traer para optimizar la query
        photo = possible_photos[0] if len(possible_photos) >= 1 else None
        if photo is not None:
            #cargar la pagina de detalle
            context = {
                'photo': photo
            }
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('No existe la foto')  # 404 Not found

class CreateView(View):
    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formulario para crear una foto
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = PhotoForm()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'photos/new_photo.html', context)

    @method_decorator(login_required())
    def post(self, request):
        """
        Crea una foto en base a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user #asigno como propietario de la foto, al usuario autenticado
        form = PhotoForm(request.POST, instance=photo_with_owner)
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