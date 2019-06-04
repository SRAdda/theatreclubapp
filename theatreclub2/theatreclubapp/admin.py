from django.contrib import admin
from .models import Lesson, Audition, Event

# Register your models here.
# Necessary if they are to appear in the admin

admin.site.register(Lesson)
admin.site.register(Audition)
admin.site.register(Event)