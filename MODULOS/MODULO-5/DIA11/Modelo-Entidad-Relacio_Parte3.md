

Cliente_id Nombre Teléfonos Código_país
1 Francisco +584121111111   +58 Venezuela
2 Felipe    +56999999999    +56 Chile
4 Felipe    +56988888888    +56 Chile                 
3 Marcos    +56977777777    +56 Chile



peliculas
 id | titulo | genero   | 
----+--------+----------+-
  1 | Inter  | Drama    |  
  2 |En busca| Ficción  | 


Peliculas_actores
 id | actor_id | peli_id   | 
----+----------+-----------+-
  1 |    1     |      1    |  
  2 |    2     |      1    | 
  3 |    3     |      2    |  
  4 |    4     |      2    | 

actores
 id | nombre | 
----+--------+-
  1 | Mano   |  
  2 | Juli   | 
  3 | Vane   | 
  4 | Jime   |



estudiantes
 id | estudiantes | cursos                    | 
----+-------------+---------------------------+-
  1 |   Juan      |     Matemática, Lengua    |  
  2 |   Mauro     |     Física, Arte          | 

## 1NF - Únicos - Atómicos
estudiantes
 id | estudiantes | cursos                    | 
----+-------------+---------------------------+-
  1 |   Juan      |     Matemática            |  
  2 |   Mauro     |     Física                | 
  3 |   Juan      |     Lengua                |  
  4 |   Mauro     |     Arte                  | 

## 2NF
No debe haber dependencia parcial -> PK

estudiantes
 id | estudiantes |
----+-------------+-
  1 |   Juan      |     
  2 |   Mauro     |    


  cursos
 id | cursos      |             
----+-------------+-
  1 |   Matemática|  
  2 |   Física    | 
  3 |   Lengua    |  
  4 |   Arte      | 

## 3NF

estudiantes
 id | estudiantes |
----+-------------+-
  1 |   Juan      |     
  2 |   Mauro     |    


  cursos
 id | cursos      |             
----+-------------+-
  1 |   Matemática|  
  2 |   Física    | 
  3 |   Lengua    |  
  4 |   Arte      | 

estudiantes_curso
 id | curso_id   |  estudiante_id            
----+------------+-----------------
  1 |     1                1
  2 |     2                2
  3 |     3                1
  4 |     4                2
