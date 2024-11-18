from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Producto 
from django.db.models import Q
from .forms import UserCreationForm

def menu(request):
    return render(request, 'pantalla/menu.html')

def registro_producto(request):
    if not request.user.is_authenticated:
        return render(request, 'pantalla/error_login.html')

    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        marca = request.POST.get('marca')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        correo = request.POST.get('correo')

        if codigo and nombre and marca and fecha_vencimiento and correo:
            if '@' in correo and '.' in correo.split('@')[-1]:
                producto = Producto(
                    codigo=codigo,
                    nombre=nombre,
                    marca=marca,
                    fecha_vencimiento=fecha_vencimiento,
                    correo=correo
                )
                producto.save()
                return render(request, 'pantalla/resultado.html', {'producto': producto})
            else:
                error_message = "El correo electrónico no tiene un formato válido."
        else:
            error_message = "Todos los campos son obligatorios."

        return render(request, 'pantalla/registro.html', {'error_message': error_message})

    return render(request, 'pantalla/registro.html')


@login_required(login_url='/login/') 
def listar_productos(request):

    productos = Producto.objects.all()
    return render(request, 'pantalla/consulta.html', {'productos': productos})


@login_required(login_url='/login/')  
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
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')

    return render(request, 'pantalla/eliminar.html', {'producto': producto})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')  
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, 'pantalla/login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 

@user_passes_test(lambda u: u.is_superuser)
def vista_admin(request):
    return render(request, 'pantalla/vista_admin.html')

@login_required
def vista_protegida(request):
    return render(request, 'pantalla/vista_protegida.html')


def crear_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('login')  
        else:
            messages.error(request, 'Error al crear el usuario. Verifica los datos.')
    else:
        form = UserCreationForm()
    
    return render(request, 'pantalla/crear_usuario.html', {'form': form})
