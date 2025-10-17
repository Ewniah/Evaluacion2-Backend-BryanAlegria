from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria

def landing_page(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {'productos': productos, 'categorias': categorias}
    return render(request, 'tienda/landing_page.html', context)

def home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    context = {'productos': productos, 'categorias': categorias}
    return render(request, 'tienda/home.html', context)

def productos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()
    context = {'productos': productos, 'categoria_actual': categoria, 'categorias': categorias}
    return render(request, 'tienda/productos_por_categoria.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    categorias = Categoria.objects.all()
    context = {'producto': producto, 'categorias': categorias}
    return render(request, 'tienda/detalle_producto.html', context)