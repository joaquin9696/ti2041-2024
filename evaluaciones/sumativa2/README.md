Evaluación 2: Formulario en Django

Este proyecto consiste en un formulario creado con Django y una base de datos en XAMPP.

Requisitos:
- Python 3.6 o superior
- pip
- Django 3.2 o superior
- XAMPP

Instrucciones de Instalación:
1. Clona el repositorio:
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. Instala Django:
   pip install django

3. Configura la base de datos en XAMPP y actualiza `settings.py` con:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'mi_base_datos',
           'USER': 'root',
           'PASSWORD': '',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }

4. Ejecuta las migraciones:
   python manage.py migrate

5. Inicia el servidor:
   python manage.py runserver

Accede a la aplicación en: http://127.0.0.1:8000/
