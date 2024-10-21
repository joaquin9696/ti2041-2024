from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto  # Importar el modelo Producto
from django.db.models import Q

def menu(request):
    return render(request, 'pantalla/menu.html')

def registro_producto(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        correo = request.POST.get('correo')

        # Validación básica
        if codigo and nombre and marca and fecha_vencimiento and correo:
            if '@' in correo and '.' in correo.split('@')[-1]:
                # Crear un nuevo producto y guardarlo en la base de datos
                producto = Producto(
                    codigo=codigo,
                    nombre=nombre,
                    marca=marca,
                    fecha_vencimiento=fecha_vencimiento,
                    correo=correo
                )
                producto.save()  # Guardar el producto en la base de datos
                return render(request, 'pantalla/resultado.html', {'producto': producto})
            else:
                error_message = "El correo electrónico no tiene un formato válido."
        else:
            error_message = "Todos los campos son obligatorios."

        return render(request, 'pantalla/registro.html', {'error_message': error_message})

    return render(request, 'pantalla/registro.html')

def listar_productos(request):
    productos = Producto.objects.all()  # Consultar todos los productos de la base de datos
    return render(request, 'pantalla/consulta.html', {'productos': productos})

def actualizar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.codigo = request.POST.get('codigo')
        producto.nombre = request.POST.get('nombre')
        producto.marca = request.POST.get('marca')
        producto.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        producto.correo = request.POST.get('correo')
        producto.save()  
        return redirect('listar_productos')  

    return render(request, 'pantalla/editar.html', {'producto': producto})


def eliminar_producto(request, id):
    # Intentar obtener el producto con el ID proporcionado
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()  # Eliminar el producto de la base de datos
        return redirect('listar_productos')  # Redirigir a la lista de productos

    return render(request, 'pantalla/eliminar.html', {'producto': producto})

