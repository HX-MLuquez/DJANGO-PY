

## DER || MER  -> UML


### RELACIONES y asignar FK - ASOCIACIONES - CARDINALIDAD

```uml
1:1   la FK puede ir en cualquier lugar 

1:N   la FK si o si debe ir en el N (MUCHOS *)

N:M  Muchos a Muchos  la FK no va en ninguna de esas tablas - sino que se crea una tabla Intermedia
*:*
```


Ejercicio MIGRAR - IMPORTAR \i 

C:/Users/mauuu/OneDrive/Escritorio/OTEC 2024/MODULO-5/DIA10/script_clientes_productos.sql

\! dir C:/

\i C:/script;

--> \i C:/script/script_clientes_productos.sql;

\i C:/Users/mauuu/OneDrive/Escritorio/OTEC 2024/MODULO-5/DIA10/script_clientes_productos.sql;


## RELACIONES

### 1 : N
```
Clientes
 id | nombre | apellido | direccion  |   dni
----+--------+----------+------------+----------
  1 | Mano   | Lopez    | Italia 32  | 2398472
  2 | Juli   | Gonzales | Brasil 232 | 65445546
  3 | Vane   | Gonzales | Mansel 1   | 12332112

Ordenes                          FK
 id  | codigo | descripcion | cliente_id |   
-----+--------+-------------+------------+
  11 |  AASD  |  arroz      |   2        | 
  23 |  SADC  |  papa,pera  |   2        | 
  32 |  AQWE  |  limon      |   1        | 

Cliente tiene muchas compras 
un Compra pertenece a un Cliente

Cliente 1 : N Orden
            FK 
```


### N : M
```
Clientes
 id | nombre | apellido | direccion  |   dni
----+--------+----------+------------+----------
  1 | Mano   | Lopez    | Italia 32  | 2398472
  2 | Juli   | Gonzales | Brasil 232 | 65445546
  3 | Vane   | Gonzales | Mansel 1   | 12332112

Favoritos                          
 id  | nombre |   
-----+--------+
  1  |  tv    |  
  3  |  celu  |  


Cliente N : M Favoritos

Acá no llevan estas tablas FK

Sino que se crea una TABLA INTERMEDIA

TABLA INTERMEDIA
Cliente_Favoritos
 id  | cliente_id |  favorito_id  |   
-----+------------+---------------+
  1  |  3         |      1
  3  |  3         |      3
  4  |  2         |      3

```


### N : M
```
colaboradores
 id | nombre | apellido | direccion  |   dni
----+--------+----------+------------+----------
  1 | Mano   | Lopez    | Italia 32  | 2398472
  2 | Juli   | Gonzales | Brasil 232 | 65445546
  3 | Vane   | Gonzales | Mansel 1   | 12332112

proyectos                         
 id  | titulo  |  
-----+---------+
  1  |  inn    |  
  3  |  bbc    |    


Colaboradores N : M Proyectos

Acá no llevan estas tablas FK

Sino que se crea una TABLA INTERMEDIA

TABLA INTERMEDIA
proyectos_colaboradores
 id  | colab_id   |  proyect_id  |   
-----+------------+--------------+
  1  |      2     |       3             
  2  |      3     |       3
     |            |     
SELECT colab_id FROM  proyectos_colaboradores WHERE proyect_id = 3;

-----|
  2
  3

[2,3]  SELECT nombre FROM colaboradores WHERE id = 2 -> Juli
SELECT nombre FROM colaboradores WHERE id = 3  -> Vane
```


colaboradores
 id | nombre | apellido | direccion  |   dni    |  titulo_proyecto
----+--------+----------+------------+----------+--------------------
  1 | Mano   | Lopez    | Italia 32  | 2398472  |  
  2 | Juli   | Gonzales | Brasil 232 | 65445546 |   bbc
  3 | Vane   | Gonzales | Mansel 1   | 12332112 |   bbc
  4 | Vane   | Gonzales | Mansel 1   | 12332112 |   inc