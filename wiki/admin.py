from django.contrib import admin
from .models import Configuration, Module, ViewType, View, Knowledge, Attachment

admin.site.register(Configuration)
admin.site.register(Module)
admin.site.register(View)
admin.site.register(ViewType)
admin.site.register(Knowledge)
admin.site.register(Attachment)
# Register your models here.
