from django.contrib import admin
from .models import movie


class adminmovie(admin.ModelAdmin):
    list_display = ['id','name','actorname','realeasedate','type','rating']

admin.site.register(movie,adminmovie)