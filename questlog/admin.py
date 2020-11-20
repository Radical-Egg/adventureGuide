from django.contrib import admin
from .models import Questlog


class QuestlogAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questTitle']}),
        ('Quest Content', {'fields': ['questContent']})
    ]


admin.site.register(Questlog)
