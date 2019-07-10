from django.contrib import admin
from .models import Configuration, Module, ViewType, View, Error

admin.site.register(Configuration)
admin.site.register(Module)
admin.site.register(View)
admin.site.register(ViewType)
admin.site.register(Error)

# Register your models here.
