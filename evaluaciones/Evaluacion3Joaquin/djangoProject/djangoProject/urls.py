from django.contrib import admin
from django.urls import path
from formularioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),  
    path('registro/', views.registro_producto, name='registro_producto'),
    path('productos/', views.listar_productos, name='listar_productos'),  
    path('productos/editar/<int:id>/', views.actualizar_producto, name='editar_producto'),  
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'), 
    path('menu/', views.menu, name='menu'),
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),  
    path('vista_admin/', views.vista_admin, name='vista_admin'), 
    path('crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('protegido/', views.vista_protegida, name='vista_protegida'),
]
