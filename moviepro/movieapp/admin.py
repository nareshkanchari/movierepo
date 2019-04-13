from django.contrib import admin
from .models import Telugu_Movies,Hindi_Movies,English_Movies
class AdminTelugu_Movies(admin.ModelAdmin):
    list_display = ['movie_name','director_name','Hero_name','Heroiene_name','producer_name','released_date']
class AdminHindi_Movies(admin.ModelAdmin):
    list_display = ['movie_name','director_name','Hero_name','Heroiene_name','producer_name','released_date']
class AdminEnglish_Movies(admin.ModelAdmin):
    list_display = ['movie_name','director_name','Hero_name','Heroiene_name','producer_name','released_date']

admin.site.register(Telugu_Movies,AdminTelugu_Movies)
admin.site.register(Hindi_Movies,AdminHindi_Movies)
admin.site.register(English_Movies,AdminEnglish_Movies)

