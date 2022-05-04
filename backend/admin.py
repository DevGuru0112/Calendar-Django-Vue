from django.contrib import admin

from backend.models import User, Date, Calendar, Entry, Resource

# Register your models here.

admin.site.register(User)
admin.site.register(Date)
admin.site.register(Calendar)
admin.site.register(Entry)
admin.site.register(Resource)