from django.contrib import admin
from django.urls import path
from formularioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registro_producto, name='home'),
    path('registro/', views.registro_producto, name='registro_producto'),
    path('productos/', views.listar_productos, name='listar_productos'),  # Lista todos los productos
    path('productos/editar/<int:id>/', views.actualizar_producto, name='editar_producto'),  # Editar productos
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),  # Eliminar productos
    path('menu/', views.menu, name='menu'),
]
