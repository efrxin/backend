from django.contrib import admin
from .models import Inscripcion


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'fecha_seminario', 'empresa', 'email', 'profesion')
    list_filter = ('fecha_seminario',)
    search_fields = ('nombre', 'empresa', 'profesion')
