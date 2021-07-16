from django.contrib import admin
from .models import Lists, Bands, Sessions, Frequencies
# Register your models here.

admin.site.register(Lists)
admin.site.register(Bands)
admin.site.register(Sessions)
admin.site.register(Frequencies)