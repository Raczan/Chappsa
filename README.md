# Proyecto Flask: Formulario de Registro de Usuarios

Este proyecto es una prueba técnica que implementa un formulario para agregar usuarios y una ruta para obtener todos los usuarios en formato JSON.

## Estructura del Proyecto

La estructura de archivos y directorios del proyecto es la siguiente:

mi_proyecto_flask/
│
├── app/
│ ├── static/
│ │ └── styles.css <-- Archivo CSS para estilos
│ │
│ ├── templates/
│ │ └── index.html <-- Archivo HTML con el formulario
│ │
│ ├── init.py <-- Archivo principal de la aplicación Flask
│ ├── routes.py <-- Archivo para definir rutas y lógica de la aplicación
│ └── create_database.sql <-- Archivo de la DB
│
└── run.py <-- Archivo para ejecutar la aplicación Flask


### Funcionalidad del Proyecto

1. **Formulario de Registro de Usuarios**: Se implementa un formulario HTML (`index.html`) que permite ingresar el nombre y correo electrónico de un nuevo usuario.

2. **Ruta `/users`**: Esta ruta devuelve todos los usuarios almacenados en la base de datos en formato JSON cuando se accede a través de un método GET.