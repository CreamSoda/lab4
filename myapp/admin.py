from django.contrib import admin
from myapp.models import Film, Cinema, Session

class FilmAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'description')
    search_fields = ['name']
    
class CinemaAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ('name', 'description', 'adress')
    search_fields = ['name']

class SessionAdmin(admin.ModelAdmin):
    list_filter = ['start']
    list_display = ('cinema', 'film', 'start', 'end')

admin.site.register(Film, FilmAdmin)
admin.site.register(Cinema, CinemaAdmin)
admin.site.register(Session, SessionAdmin)
