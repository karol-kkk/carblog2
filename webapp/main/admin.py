from django.contrib import admin
from .models import Event, Round
# Register your models here.

class RoundInline(admin.TabularInline):
    model = Round
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [RoundInline]

admin.site.register(Event, EventAdmin)
