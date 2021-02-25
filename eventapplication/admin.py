from django.contrib import admin


# Register your models here.
from .models import participant
from .models import participantadmin
admin.site.register(participant,participantadmin)