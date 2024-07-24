
# Diagrama de Entidad-Relación de la Base de Datos `citas_medicas`

```bash
    ┌────────────────┐     ┌───────────────┐     ┌──────────────┐
    │  Especialistas │     │  CentroMedico │     │    Usuarios  │
    │ -------------- │     │ ------------- │     │ ------------ │
    │  id            │     │  id           │     │  id          │
    │  nombre        │     │  nombre       │     │  email       │
    │  especialidad  │     │  direccion    │     │  password    │
    │                │     │               │     │  tipo_usuario│
    └────────────────┘     └───────────────┘     └──────────────┘
             │                    │                      │
             │                    │                      │
             └────────┬───────────┘                      │
                      │                                  │
                      ▼                                  │
             ┌──────────────────┐                        │
             │       Agendas    │                        │
             │ ---------------- │                        │
             │  id              │                        │
             │  fecha_disponible│                        │
             │  hora_disponible │                        │
             │  especialista_id │                        │
             │  centro_medico_id│                        │
             └──────────────────┘                        │
                      │                                  │
                      │                                  │
                      ▼                                  │
        ┌──────────────┐                                 │
        │      Citas   │                                 │
        │  ----------- │                                 │
        │  id          │                                 │
        │  agenda_id   │◀───────────────────────────────┘
        │  usuario_id  │
        │  mensaje     │
        └──────────────┘
            ▲
            │
            │  ¿? Puede solicitar una cita o No (determinar)
            ▼  o puede consultar por agenda o especialistas en tal centro médico
        ┌──────────────┐
        │    Contactos │
        │ ------------ │
        │  id          │
        │  nombre      │
        │  email       │
        │  mensaje     │
        └──────────────┘
```