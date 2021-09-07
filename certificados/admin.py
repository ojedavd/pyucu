from django.contrib import admin
from .models import Certificado

# Register your models here.  
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('dni', 'name', 'description', 'published')

# Register the admin class with the associated model
admin.site.register(Certificado, CertificadoAdmin)