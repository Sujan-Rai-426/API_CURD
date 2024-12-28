from django.contrib import admin

from Home.models import Note, Transaction

# Register your models here.

admin.site.register(Note)
admin.site.register(Transaction)