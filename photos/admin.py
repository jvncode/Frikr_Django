from django.contrib import admin
from photos.models import Photo


class PhotoAdmin(admin.ModelAdmin):

    list_display = ('name', 'owner_name', 'license', 'visibility')
    list_filter = ('license', 'visibility')
    search_fields = ('name', 'description')

    def owner_name(self, obj):
        return '{} {}'.format(obj.owner.first_name, obj.owner.last_name)
    owner_name.short_description = 'Photo owner'  #Atributo a un metodo de una clase. Este permite poner el nombre que queramos a la columna owner_name
    owner_name.admin_order_field = 'owner'       #Atributo a un metodo de una clase. Este permite dar un orden a la columna owner

    # Con fieldsets definimos los campos individuales de cada entrada(foto en este caso)
    fieldsets = (
        (None, {
            'fields': ('name',),  #Determina los campos que queremos en este apartado
            'classes': ('wide',)  #Determina el CSS que queremos aplicarle a dichos campos
        }),
        ('Description & Autor', {
            'fields': ('description', 'owner'),
            'classes': ('wide',)   #La clase wide hace que los campos se alineen
        }),
        ('Extra', {
            'fields': ('url', 'license', 'visibility'),
            'classes': ('wide', 'collapse')  #La clase collapse hace que el plegue en un menú 'mostrar' los 3 campos especificados en este apartado
        })

    )

admin.site.register(Photo, PhotoAdmin)
