from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('tienda/', views.home, name='home'),   
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
]