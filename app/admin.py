from django.contrib import admin
from .models import TB_Autor, TB_Livro

# Register your models here.
admin.site.register(TB_Livro)
admin.site.register(TB_Autor)
