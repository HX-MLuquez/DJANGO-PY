### Tabla Inicial

**Tabla "Empleados"**

| EmpleadoID | Nombre | Departamento   | Jefe  | Ubicación | Turno          |
|------------|--------|----------------|-------|-----------|----------------|
| 1          | Juan   | Ventas         | María | Ciudad A  | mañana         |
| 2          | María  | Ventas         | NULL  | Ciudad A  | tarde          |
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B | mañana, tarde  |


| EmpleadoID | Nombre | Departamento   | Jefe  | Ubicación | Turno          |
|------------|--------|----------------|-------|-----------|----------------|
| 1          | Juan   | Ventas         | María | Ciudad A  | mañana         |
| 2          | María  | Ventas         | NULL  | Ciudad A  | tarde          |
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B | mañana         |
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B | tarde          |


| EmpleadoID | Nombre | Departamento   | Jefe  | Ubicación | Turno1          | Turno2          |
|------------|--------|----------------|-------|-----------|-----------------|-----------------|
| 1          | Juan   | Ventas         | María | Ciudad A  | mañana          |
| 2          | María  | Ventas         | NULL  | Ciudad A  |                 |  tarde
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B | mañana          |  tarde 

## 1FN - creamos la tabla Turnos y su relación N:M con su tabla intermedia
**Tabla "Empleados"**
| EmpleadoID | Nombre | Departamento   | Jefe  | Ubicación | 
|------------|--------|----------------|-------|-----------|
| 1          | Juan   | Ventas         | María | Ciudad A  | 
| 2          | María  | Ventas         | NULL  | Ciudad A  | 
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B | 



**Tabla "Turnos"**
| turno_id | Nombre | 
|----------|--------|
| 1        | mañana |
| 2        | tarde  |

**Tabla "Turno_Empleado"**
| id | turno_id |  empleado_id |
|----------|--------|--------|
| 1        | 1 |  1 |
| 2        | 2  | 2  |
| 3        | 1 |  3 |
| 4        | 2  | 3  |


## 2FN - Dependencia Parcial - creamos la tabla Departamento y su relación 1:N
**Tabla "Empleados"**
| EmpleadoID | Nombre | Departamento   | Jefe  | Ubicación |  departamento_id  |
|------------|--------|----------------|-------|-----------|-----------|
| 1          | Juan   | Ventas         | María | Ciudad A  |  1     |
| 2          | María  | Ventas         | NULL  | Ciudad A  |  1     |
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B |  2     |


**Tabla "Departamento"**
| id  | Departamento   | Jefe  | Ubicación | 
|------------|----------------|-------|-----------|
| 1         | Ventas         | María | Ciudad A  | 
| 2         | Contabilidad   | Roberto| Ciudad B | 


**Tabla "Turnos"**
| turno_id | Nombre | 
|----------|--------|
| 1        | mañana |
| 2        | tarde  |

**Tabla "Turno_Empleado"**
| id | turno_id |  empleado_id |
|----------|--------|--------|
| 1        | 1 |  1 |
| 2        | 2  | 2  |
| 3        | 1 |  3 |
| 4        | 2  | 3  |


## 3FN - Dependencia transitiva - creamos la tabla Jefes y su relación 1:N
**Tabla "Empleados"**
| EmpleadoID | Nombre | Departamento   | Jefe  | Ubicación |  departamento_id  |
|------------|--------|----------------|-------|-----------|-----------|
| 1          | Juan   | Ventas         | María | Ciudad A  |  1     |
| 2          | María  | Ventas         | NULL  | Ciudad A  |  1     |
| 3          | Pedro  | Contabilidad   | Roberto| Ciudad B |  2     |


**Tabla "Departamento"**
| id  | Departamento     | Ubicación |    jefe_id  |
|------------|---------------|---------|-----------|
| 1         | Ventas         | Ciudad A  |  1      |
| 2         | Contabilidad   | Ciudad B |   2      |

**Tabla "Jefes"**
| id  | Jefe  |
|-----|-----------|
| 1   |  María | 
| 2   | Roberto | 


**Tabla "Turnos"**
| turno_id | Nombre | 
|----------|--------|
| 1        | mañana |
| 2        | tarde  |

**Tabla "Turno_Empleado"**
| id | turno_id |  empleado_id |
|----------|--------|--------|
| 1        | 1 |  1 |
| 2        | 2  | 2  |
| 3        | 1 |  3 |
| 4        | 2  | 3  |
