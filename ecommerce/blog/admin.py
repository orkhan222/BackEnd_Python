from django.contrib import admin
from django.db.models.deletion import CASCADE
from . models import Post,Commet


# Register your models here.

admin.site.register(Post)
admin.site.register(Commet)