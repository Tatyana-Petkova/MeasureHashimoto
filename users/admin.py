from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(RegisteredUser)
admin.site.register(Results)
admin.site.register(ImportedResults)
