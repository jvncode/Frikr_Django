from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

def badwords_detector(value):
    """
    Valida si en 'value' se han puesto tacos definidos en settings.BADWORDS
    :return: Boolean
    """
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError('La palabra {} no está permitida'.format(badword))

    #Si todo va OK, devuelvo True
    return True
