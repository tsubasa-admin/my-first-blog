from django.contrib import admin

from nodolist.models import Image, Post, Tag

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Image)