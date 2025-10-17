from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin): # Esto permite que se puedan visualizar en columnas
    list_display = ('id', 'nombre', 'precio', 'stock', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre', 'descripcion')
