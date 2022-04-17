from django.contrib import admin

from neighbourhood.models import Business, Neighbourhood, Post, Profile

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Post)