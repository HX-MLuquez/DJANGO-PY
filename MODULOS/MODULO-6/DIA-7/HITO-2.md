# HITO-2

**HITO-2** Creación de un sitio web responsive con Bootstrap: en este Hito se crearán las primeras estructuras que permitirán mostrar datos en nuestro sitio web.

### Implementar

- **BOOTSTRAP**: Crear sitio web responsive con Bootstrap
- **STATIC**: Implementa un proyecto Django para servir contenido estático dando solución a los requerimientos. Implementar **load static a todo el documento** y marcar sintaxis de static cual: {% static 'path' %}
- **TEMPLATES**: Utiliza templates para la renderización de contenido dinámico en un proyecto Django para dar solución a un requerimiento.
  - VARIABLES
  - CONDICIONALES
  - HERENCIA: Utiliza herencia de plantillas en un proyecto Django para dar solución a un requerimiento. Django permite la reutilización de una plantilla dentro de otra.
  - LOOP (bucle FOR)
- **LOGIN-isActivate**: Utiliza instrucciones de control en plantillas de un proyecto Django para dar solución a un requerimiento.
  - Filtro if + | filter UPERCASE

---

### PASOS

1. Crear una plantilla o template base que tendrá los elementos comunes de la interfaz de nuestro sitio web OnlyFlans.
  - about
  - index
  - base
  - navbar
  - header
  - footer
  - welcome

2. Habilitar las rutas o url: /, /acerca y /bienvenido, creando las vistas y plantillas necesarias que extiendan la plantilla base para mostrar diferentes contenidos para cada vista.

3. Como elementos transversales mínimos que deberán mostrarse en todas las rutas se
   encuentran: - header, que contenga un logo para nuestra web - navbar, que permita la navegación entre las distintas rutas de nuestra web - footer, que entregue la información de “desarrollado por” incluyendo tu nombre y la frase “para Desafío Latam”, ejemplo: “desarrollado por Juan Perez para Desafío Latam”

4. Adicionalmente cada ruta deberá mostrar lo siguiente:
   - ruta /: deberá mostrar una lista de productos disponibles para la venta en la tienda de la PYME.
   - ruta /acerca: deberá mostrar una descripción de la utilidad del sitio web, junto con la descripción de la PYME y datos como la fecha de creación, entre otros que se dispongan.
   - ruta /bienvenido: deberá mostrar un mensaje de “bienvenido cliente” genérico en caso de no contar con los datos de un usuario y un mensaje de “bienvenido Juan Perez”(nombre variable) en el caso de contar con los datos del mismo.

Para la mejor visualización del sitio web que estamos creando se debe utilizar tanto la “grilla” de bootstrap como sus componentes, permitiendo al sitio web “acomodarse” a distintos tamaños de pantalla y resoluciones, además de permitir su rápido desarrollo. Puedes valerte de componentes de bootstrap como navbar, tarjetas o cards, entre otros según desees.


```
```

## IMPORTANTE
Para mostrar los productos en el home (index.html nuestro) usamos una lista dentro del mismo views. 

# EXTRAS
- Ver como crear un model (+ migrate), como ver o eliminar datos desde el admin o como acceder a los datos de un modelo desde una view.
- Recordar como hacemos formularios como antes usando label, input y demás y ver como Forms de Django nos simplifica esto y nos brinda ya validaciones 




```
```

### SUPER EXTRAS
- Envío de email