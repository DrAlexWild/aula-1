from django.contrib import admin

# Register your models here.
from .models import Tarefa
from .models import Blog_Post

admin.site.register(Tarefa)
admin.site.register(Blog_Post)