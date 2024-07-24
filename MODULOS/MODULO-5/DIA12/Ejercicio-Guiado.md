- **1NF - Atomicidad**


- **2NF - Dependencia Parcial**: ID 
  - Dependencia parcialmente funcional
  - Dependencia no completa

- **3NF - Dependencia Transitiva**:  A <- B <- C (depende de B pero no de A)
  - Dependencia indirecta
  - Dependencia de tercer nivel



Ejercicio 

| Matrícula | Nombre    | Email                  | Teléfono   | Curso                          | Carrera              |
|-----------|-----------|------------------------|------------|--------------------------------|----------------------|
| 1         | Francisco | francisco@francisco.com | 56955555555 | Introducción al desarrollo web, Programación con Ruby , Bases de datos, Introducción a Ruby on Rails  | Emprendedor Digital  |
| 2         | Felipe    | felipe@felipe.com       | 56944444444 | Introducción al desarrollo web | Full Stack JavaScript|



| Matrícula | Nombre    | Email                  | Teléfono   | Curso                          | Carrera              |
|-----------|-----------|------------------------|------------|--------------------------------|----------------------|
| 1         | Francisco | francisco@francisco.com | 56955555555 | Introducción al desarrollo web | Emprendedor Digital  |
| 1         | Francisco | francisco@francisco.com | 56955555555 | Programación con Ruby          | Emprendedor Digital  |
| 1         | Francisco | francisco@francisco.com | 56955555555 | Bases de datos                 | Emprendedor Digital  |
| 1         | Francisco | francisco@francisco.com | 56955555555 | Introducción a Ruby on Rails   | Emprendedor Digital  |
| 2         | Felipe    | felipe@felipe.com       | 56944444444 | Introducción al desarrollo web | Full Stack JavaScript|


| Matrícula | Nombre    | Email                  | Teléfono   | Curso_1           | Curso_2 | |Carrera              |
|-----------|-----------|------------------------|------------|--------|------------|------------------------|----------------------|
| 1         | Francisco | francisco@francisco.com | 56955555555 | Introducción al desarrollo web, Programación con Ruby  | Emprendedor Digital  |
| 2         | Felipe    | felipe@felipe.com       | 56944444444 | Introducción al desarrollo web | | | | Full Stack JavaScript|




## 1FN -> Crear nueva Tabla Curso

**Estudiante**

| Matrícula | Nombre    | Email                  | Teléfono   | Carrera              |
|-----------|-----------|------------------------|------------|----------------------|
| 1         | Francisco | francisco@francisco.com | 56955555555 |  Emprendedor Digital  |
| 2         | Felipe    | felipe@felipe.com       | 56944444444 |  Full Stack JavaScript|

**Curso**

| Curso_id | Nombre_curso               | Matrícula |
|----------|----------------------------|-----------|
| 1        | Introducción al desarrollo web | 1         |
| 2        | Programación con Ruby      | 1         |
| 3        | Bases de datos             | 1         |
| 4        | Introducción a Ruby on Rails| 1         |
| 1        | Introducción al desarrollo web | 2         |


## 2FN -> Relación Tabla Intermedia

**Estudiante**

| Matrícula | Nombre    | Email                  | Teléfono   | Carrera              |
|-----------|-----------|------------------------|------------|----------------------|
| 1         | Francisco | francisco@francisco.com | 56955555555 |  Emprendedor Digital  |
| 2         | Felipe    | felipe@felipe.com       | 56944444444 |  Full Stack JavaScript|

**Curso**

| Curso_id | Nombre_curso               |
|----------|----------------------------|
| 1        | Introducción al desarrollo web | 
| 2        | Programación con Ruby      | 
| 3        | Bases de datos             | 
| 4        | Introducción a Ruby on Rails| 


**Estudiante_Curso**
| id | matricula_id               |   curso_id  |
|----------|----------------------------|--------------|
| 1        | 1 |  1 |
| 2        | 1  | 2 |
| 3        | 1  | 3 |
| 4        | 1 | 4 |
| 5        | 2 | 1 |



## 3FN -> Dependencia Transitiva - Creamos tabla carrera 

**Estudiante**

| Matrícula | Nombre    | Email                  | Teléfono   | 
|-----------|-----------|------------------------|------------|
| 1         | Francisco | francisco@francisco.com | 56955555555 |  
| 2         | Felipe    | felipe@felipe.com       | 56944444444 | 

**Curso**

| Curso_id | Nombre_curso               |
|----------|----------------------------|
| 1        | Introducción al desarrollo web | 
| 2        | Programación con Ruby      | 
| 3        | Bases de datos             | 
| 4        | Introducción a Ruby on Rails| 


**Estudiante_Curso**
| id | matricula_id   |  curso_id  |
|----------|---------|--------------|
| 1        | 1 |  1 |
| 2        | 1  | 2 |
| 3        | 1  | 3 |
| 4        | 1 | 4 |
| 5        | 2 | 1 |

**Carrera**

| carrera_id |  Carrera              |
|-----------|----------------------|
| 1         |   Emprendedor Digital  |
| 2         |   Full Stack JavaScript|


**Estudiante_Carrera**
| id | matricula_id   |  carrera_id  |
|----------|---------|--------------|
| 1        | 1 |  1 |
| 2        | 2  | 2 |
