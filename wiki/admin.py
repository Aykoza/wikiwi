from django.contrib import admin
from .models import Configuration, Module, ViewType, View, Error, HotelRooms

admin.site.register(Configuration)
admin.site.register(Module)
admin.site.register(View)
admin.site.register(ViewType)
admin.site.register(Error)
admin.site.register(HotelRooms)
# Register your models here.
