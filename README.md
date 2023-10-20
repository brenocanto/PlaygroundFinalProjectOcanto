# PlaygroundFinalProjectOcanto

## Video demostracion de la página: https://drive.google.com/file/d/1AgcJxid06nZT9lenYFI9IUM-xosrML9F/view?usp=sharing

## Instalación:
Para los primeros 4 puntos (**Instalación y ejecución**), es necesario abrir una terminal y posicionarse en el directorio donde se descargó el proyecto.

1. El proyecto fue realizado con un entorno virtual por lo que para mejor ejecucion es preferible tenerlo activo "python -m venv venv" y luego "source venv/Scripts/activate"
2. Luego del paso anterior, debe contar con las librerías detalladas en *requirements.txt*. En caso de NO contar con ellas, ejecutar ***pip install -r requirements.txt***.

#

## Ejecución
1. Para la ejecución del proyecto, tipear ***python manage.py runserver 4000***, y luego dirigirse a su navegador.

#

## Secciones y funcionalidades
1. Clickeando sobre *El rincón Swiftie* usted podrá dirigirse a la página de inicio, sin importar en que sección se encuentre. Lo mismo sucederá al presionar *Inicio*.
2. El blog cuenta con las diferentes secciones *Canciones*, *Chat*(unicamente al estar logueado), *Iniciar Sesión*,*Registrarse*.
3. En el pie de página se encuentran las secciones *Acerca de mí*, *Contacto*, *Terminos de Uso*, *Politicas de Privacidad*. Por lo pronto no hay información en estas paginas, salvo en *Acerca de mi* donde podrán ver un breve comentario de la autora de la página.
4. El sistema permite la gestión de usuarios. En las secciones de: *Iniciar sesión* y *Registrarme*. En caso de NO estar logueado, se podrá navegar por la web pero con funcionalidades reducidas. Luego de iniciar sesión, podrá dirigirse a *Chat*,  *Mi perfil*(clickeando sobre el nombre de usuario), *Editar perfil* y *Cambiar contraseña*(las 2 ultimas funcionalidad internas de "Mi perfil")
5. En la sección *Canciones*, podrá visualizar el listado de canciones ya ingresadas al sistema y contará con diferentes opciones para gestionar cada una de ellas: *Ingresas nueva canción*, *Buscar*.
Si sos el usuario autor de una de las publicaciones de la letra de una canción podras visualizar los botones de *Editar* y *Eliminar*, mientras no seas el autor unicamente podrás visualizarlo.
6. Desde la sección *Chat*, podrás iniciar conversaciones con los diferentes usuarios que formen parte del sistema.

#