from django.contrib import admin
from .models import Configuration, Module, ViewType, View

admin.site.register(Configuration)
admin.site.register(Module)
admin.site.register(View)
admin.site.register(ViewType)

# Register your models here.
