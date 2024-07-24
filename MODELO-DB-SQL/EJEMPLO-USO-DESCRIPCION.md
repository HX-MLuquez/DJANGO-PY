## Descripción de las tablas

1. **Contactos**
   - **Función**: Almacena información de las personas que se ponen en contacto con la clínica o el hospital a través de un formulario de contacto.
   - **Ejemplo**: Un paciente potencial envía una consulta sobre los horarios disponibles para una cita médica.

2. **Usuarios**
   - **Función**: Almacena la información de los usuarios registrados en el sistema, incluyendo pacientes y médicos.
   - **Ejemplo**: Un paciente se registra en el sistema con su correo electrónico y una contraseña para acceder a los servicios médicos.

3. **Especialistas**
   - **Función**: Almacena información sobre los médicos especialistas que trabajan en la clínica o el hospital.
   - **Ejemplo**: La clínica tiene un cardiólogo y un pediatra en su equipo de especialistas.

4. **CentroMedico**
   - **Función**: Almacena información sobre los centros médicos o clínicas, incluyendo sus nombres y direcciones.
   - **Ejemplo**: La clínica "Hospital Central" se encuentra en "Calle Falsa 123".

5. **Agendas**
   - **Función**: Almacena los horarios disponibles de los especialistas para las citas médicas.
   - **Ejemplo**: El Dr. Ramirez está disponible para consultas el 20 de julio de 2024 a las 9:00 am.

6. **Citas**
   - **Función**: Almacena información sobre las citas médicas programadas, incluyendo el usuario (paciente), el horario y el especialista.
   - **Ejemplo**: Un paciente programa una cita con el Dr. Ramirez el 20 de julio de 2024 a las 9:00 am.

---

## Ejemplo de uso en un entorno real

Imagina una clínica llamada "Hospital Central" que tiene varios especialistas y ofrece a los pacientes la posibilidad de reservar citas médicas en línea. A continuación, se presenta un flujo de cómo funcionan estas tablas en un entorno real:

1. **Registro de un contacto**: Juan Perez visita el sitio web de "Hospital Central" y envía una consulta a través del formulario de contacto preguntando sobre la disponibilidad de citas.
   - **Tabla afectada**: Contactos
   - **Registro añadido**:
     ```plaintext
     id: 1
     nombre: Juan Perez
     email: juan@example.com
     mensaje: Consulta sobre disponibilidad de citas.
     ```

2. **Registro de un usuario**: Juan decide registrarse en el sistema para poder reservar una cita.
   - **Tabla afectada**: Usuarios
   - **Registro añadido**:
     ```plaintext
     id: 1
     email: juan@example.com
     password: password123
     tipo_usuario: paciente
     ```

3. **Añadir un especialista**: La clínica registra a un nuevo cardiólogo, el Dr. Ramirez.
   - **Tabla afectada**: Especialistas
   - **Registro añadido**:
     ```plaintext
     id: 1
     nombre: Dr. Ramirez
     especialidad: Cardiología
     ```

4. **Añadir un centro médico**: La clínica se asegura de que su información está registrada en el sistema.
   - **Tabla afectada**: CentroMedico
   - **Registro añadido**:
     ```plaintext
     id: 1
     nombre: Hospital Central
     direccion: Calle Falsa 123
     ```

5. **Programar la agenda del especialista**: El Dr. Ramirez tiene disponible el 20 de julio de 2024 a las 9:00 am.
   - **Tabla afectada**: Agendas
   - **Registro añadido**:
     ```plaintext
     id: 1
     fecha_disponible: 2024-07-20
     hora_disponible: 09:00:00
     especialista_id: 1
     centro_medico_id: 1
     ```

6. **Reservar una cita**: Juan reserva una cita con el Dr. Ramirez para una revisión general el 20 de julio de 2024 a las 9:00 am.
   - **Tabla afectada**: Citas
   - **Registro añadido**:
     ```plaintext
     id: 1
     agenda_id: 1
     usuario_id: 1
     mensaje: Revisión general.
     ```

### Conexión de las tablas

- **Contactos** permite a la clínica recibir consultas y mensajes de personas interesadas en sus servicios.
- **Usuarios** gestiona los datos de pacientes y médicos registrados en el sistema.
- **Especialistas** almacena la información de los médicos disponibles.
- **CentroMedico** mantiene los datos de los diferentes centros médicos.
- **Agendas** organiza los horarios disponibles para las consultas médicas.
- **Citas** registra las citas médicas que los pacientes han programado con los especialistas.

Este flujo ilustra cómo las tablas interaccionan entre sí para permitir la gestión de una clínica médica, desde la recepción de consultas hasta la programación de citas médicas.