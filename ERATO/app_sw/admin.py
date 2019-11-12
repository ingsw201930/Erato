from django.contrib import admin
from .models import SW, Service,Tag,Appearance
# Register your models here.

admin.site.register(SW)
admin.site.register(Service)
admin.site.register(Tag)
admin.site.register(Appearance)
