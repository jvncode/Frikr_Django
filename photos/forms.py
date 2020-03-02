from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

class PhotoForm(forms.ModelForm):
    """
    Formulario para el modelo Photo
    """
    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Valida si en la descripción se han puesto tacos definidos en settings.BADWORDS
        :return: diccionario con los atributos si OK
        """
        cleaned_data = super(PhotoForm, self).clean() #llamada a la superclase de Django

        description = cleaned_data.get('description', '') #devuelve lo que hay en el diccionario 'description', y si no existe me devuelve una cadena vacia

        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('La palabra {} no está permitida'.format(badword))

        #Si todo va OK, devuelvo los datos limpios/normalizados
        return cleaned_data


