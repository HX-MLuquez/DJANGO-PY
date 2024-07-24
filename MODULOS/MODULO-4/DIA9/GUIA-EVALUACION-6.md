# Diagrama de Clases

## Clases y Relaciones

# Diagrama de Clases

```plaintext
---------------------
|    Producto        |
---------------------
| - __nombre: str    |
| - __precio: float  |
| - __stock: int     |
---------------------
| + nombre: str      |
| + precio: float    |
| + stock:int & sett |
---------------------
| + __add__()        |
| + __sub__()        |
| + __eq__()         |
---------------------

                 |
                 |
                 v

---------------------------------------------------------------
|      Tienda                                                 |
---------------------------------------------------------------
| <<abstract>>                                                |
---------------------------------------------------------------
| + ingresar_producto(nombre: str, precio: float, stock: int) |
| + listar_productos(): str                                   |
| + realizar_venta(nombre_producto: str, cantidad: int)       |
--------------------------------------------------------------
      ▲                        ▲                    ▲
     /                         |                     \
    /                          |                      \
   /                           |                       \
  v                            v                        v
---------------------      -----------------------     ---------------------
| TiendaRestaurante  |     |   TiendaFarmacia    |     | TiendaSupermercado |
---------------------      -----------------------     ---------------------
| + tipo: str        |     | + tipo: str         |     | + tipo: str        |
| - __nombre: str    |     | - __nombre: str     |     | - __nombre: str    |
| - __costo_delivery |     |- __costo_delivery   |     |- __costo_delivery  |
|          : float   |     |           : float   |     |                    |
| - __productos: list|     | - __productos: list |     | - __productos: list|
---------------------      -----------------------     ----------------------
| + ingresar_producto(nombre: str, precio: float, stock: int) |  <- APPEND  (Composición)
| + listar_productos(): str                                   |  <- FOR
| + realizar_venta(nombre_producto: str, cantidad: int)       |  <- Se pasa info de producto, se crea, se  
|                                      compara con los que hay por == por nombre, se restan (se resta stock)
--------------------------------------------------------------|         SOBRECARGA  + (Composición)
```

```mermaid
classDiagram
    TiendaRestaurante -> Utiliza (Composición) -> Producto
    TiendaFarmacia : Utiliza (Composición) -> Producto
    TiendaSupermercado : Utiliza (Composición) -> Producto
    TiendaRestaurante --|> Tienda
    TiendaFarmacia --|> Tienda
    TiendaSupermercado --|> Tienda

    class Producto {
        -nombre: str
        -precio: float
        -stock: int
        +__add__(Producto): int
        +__sub__(Producto): int
        +__eq__(Producto): bool
    }

    class Tienda {
        <<abstract>>
        +ingresar_producto(nombre: str, precio: float, stock: int)
        +listar_productos(): str
        +realizar_venta(nombre_producto: str, cantidad: int)
    }

    class TiendaRestaurante {
        +tipo: str = "Restaurante" (estático)
        -nombre: str
        -costo_delivery: float
        -productos: list
        ----------------------------------------
        +ingresar_producto(nombre: str, precio: float, stock: int)
        +listar_productos(): str
        +realizar_venta(nombre_producto: str, cantidad: int)  -  pass
    }

    class TiendaFarmacia {
        +tipo: str = "Farmacia"
        -nombre: str
        -costo_delivery: float
        -productos: list
        ----------------------------------------
        +ingresar_producto(nombre: str, precio: float, stock: int)
        +listar_productos(): str
        +realizar_venta(nombre_producto: str, cantidad: int)
    }

    class TiendaSupermercado {
        +tipo: str = "Supermercado"
        -nombre: str
        -costo_delivery: float
        -productos: list
        ----------------------------------------
        +ingresar_producto(nombre: str, precio: float, stock: int)
        +listar_productos(): str
        +realizar_venta(nombre_producto: str, cantidad: int)
    }
```

# MENÚ

```bash
int(input("Ingrese tipo de la tienda a agregar:\n"
                 "1. Restaurante\n2. Supermercado\n3. Farmacia\n"))
input("\nIngrese nombre de la tienda a agregar:\n")
int(input("\nIngrese precio del deliveyr:\n"))

CREAR la TIENDA CORRESPONDIENTE

input("\nIngrese nombre del producto a ingresar:\n")
int(input("\nIngrese precio del producto:\n"))
int(input("\nIngrese stock del producto:\n"))

AGREGAR PRODUCTO A LA TIENDA y MIENTRAS EL USUARIO QUIERA SEGUIR AGREGANDO DAR LA OPCIÓN
int(input("\n¿Desea agregar otro producto?\n"
                       "1. Sí\n2. No\n"))



int(input("\nIndique qué desea realizar:\n"
            "1. Listar productos de la tienda\n"
            "2. Realizar una venta de producto\n"
            "3. Salir\n"))

LISTAR, VENDER PRODUCTO o SALIR

VENTA (para VENTA)
input("\nIngrese nombre del producto a vender:\n")
int(input("\nIngrese cantidad que desea comprar:\n"))
        tienda.realizar_venta(nombre_producto, cantidad)

MIENTRAS el USUARIO quiera seguir VENDIENDO o MIRANDO la LISTA dar opción
int(input("\nIndique qué desea realizar:\n"
            "1. Listar productos de la tienda\n"
            "2. Realizar una venta de producto\n"
            "3. Salir\n"))
FIN
```

# Descripción de Clases y Métodos

## Clase Producto
### Atributos Privados

- __nombre: Nombre del producto.
- __precio: Precio del producto.
- __stock: Cantidad en stock del producto. Devuelve y establece el stock del producto. Si el stock es menor o igual a 0, se establece en 0.

### Métodos

- __init__(self, nombre, precio, stock=0): Inicializa un producto con nombre, precio y stock.
- __add__(self, other): Suma el stock de dos productos.
- __sub__(self, other): Resta el stock de dos productos.
- __eq__(self, other): Compara dos productos por su nombre.

## Clase Abstracta Tienda
### Métodos Abstractos
- ingresar_producto(self, nombre, precio, stock): Debe ser implementado para ingresar un producto.
- listar_productos(self): Debe ser implementado para listar productos.
- realizar_venta(self, nombre_producto, cantidad): Debe ser implementado para realizar una venta.

## Clase TiendaRestaurante (Heredada de Tienda)
### Atributos

- tipo: Tipo de tienda, en este caso "Restaurante".
- __nombre: Nombre del restaurante.
- __costo_delivery: Costo de delivery.
- __productos: Lista de productos del restaurante.

### Métodos

- ingresar_producto(self, nombre, precio, stock): Ingresa un producto a la lista de productos del restaurante.
- listar_productos(self): Lista los productos del restaurante.
- realizar_venta(self, nombre_producto, cantidad): Realiza una venta de un producto (aún no implementado).

## Clase TiendaFarmacia (Heredada de Tienda)
### Atributos

- tipo: Tipo de tienda, en este caso "Farmacia".
- __nombre: Nombre de la farmacia.
- __costo_delivery: Costo de delivery.
- __productos: Lista de productos de la farmacia.

### Métodos

- ingresar_producto(self, nombre, precio, stock): Ingresa un producto a la lista de productos de la farmacia. Si el producto ya existe, actualiza el stock.
- listar_productos(self): Lista los productos de la farmacia, indicando si hay envío gratis para productos caros.
- realizar_venta(self, nombre_producto, cantidad): Realiza una venta de un producto, permitiendo comprar hasta 3 unidades.

## Clase TiendaSupermercado (Heredada de Tienda)
### Atributos

- tipo: Tipo de tienda, en este caso "Supermercado".
- __nombre: Nombre del supermercado.
- __costo_delivery: Costo de delivery.
- __productos: Lista de productos del supermercado.

### Métodos

- ingresar_producto(self, nombre, precio, stock): Ingresa un producto a la lista de productos del supermercado. Si el producto ya existe, actualiza el stock.
- listar_productos(self): Lista los productos del supermercado, indicando si hay pocos productos disponibles.
- realizar_venta(self, nombre_producto, cantidad): Realiza una venta de un producto, actualizando el stock.


**Herencia y Polimorfismo:** La clase Tienda es abstracta y define métodos que deben ser implementados por las clases concretas TiendaRestaurante, TiendaFarmacia y TiendaSupermercado. Esto permite utilizar polimorfismo para manejar diferentes tipos de tiendas de manera uniforme.

**Encapsulamiento:** Se utilizan atributos privados y propiedades para controlar el acceso y la modificación de los atributos de las clases.

**Sobrecarga de Operadores:** La clase Producto sobrecarga los operadores de adición y sustracción para manejar el stock de manera conveniente, y el operador de igualdad para comparar productos por su nombre.


