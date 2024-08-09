# FORM en DJANGO

## Partes de un Form

- {% csrf_token %}: Este token es necesario en formularios POST en Django para proteger contra ataques CSRF (Cross-Site Request Forgery).

- {{ form.as_p }}: Este código renderiza todos los campos del formulario utilizando etiquetas <p>, lo que genera un formulario básico y sencillo.

- Botón de Enviar (<button type="submit">Enviar</button>): Este botón envía el formulario cuando se hace clic en él.

---

**La action tipo action="/contacto_model_form" no es necesaria?**

En la mayoría de los casos, no es necesario especificar el atributo action en la etiqueta <form>. Si no se especifica action, el formulario se enviará a la misma URL de la página en la que se encuentra, lo que es útil y común en muchas aplicaciones.

---
### .as_table como .as_p

Puedes usar tanto .as_table como .as_p con un formulario basado en forms.Form, como en el caso de tu ContactFormForm. Estos métodos de renderizado de Django permiten presentar el formulario en diferentes formatos sin tener que escribir HTML personalizado.

---

# `forms.Form` como `forms.ModelForm` se utilizan para manejar formularios, pero tienen diferentes propósitos y características. Aquí te explico las principales diferencias entre ellos:

### `forms.Form`

- **Propósito General**: `forms.Form` se utiliza para crear formularios que no están directamente vinculados a un modelo de base de datos. Es útil cuando necesitas un formulario para propósitos distintos a la entrada de datos en una tabla de la base de datos.

- **Definición**: En un formulario basado en `forms.Form`, defines los campos y la validación de los datos directamente en el formulario. Los datos no se guardan automáticamente en la base de datos; tú eres responsable de manejar el almacenamiento de datos.

- **Ejemplo**:

  ```python
  from django import forms

  class ContactForm(forms.Form):
      customer_email = forms.EmailField(label='Correo')
      customer_name = forms.CharField(max_length=64, label='Nombre')
      message = forms.CharField(label='Mensaje')
  ```

- **Uso Típico**: Formularios para búsquedas, suscripciones, o entradas que no requieren persistencia en una base de datos.

### `forms.ModelForm`

- **Propósito Específico**: `forms.ModelForm` se utiliza para crear formularios basados en un modelo de Django. Facilita la creación, edición y validación de instancias de un modelo y automáticamente maneja la conversión entre el formulario y el modelo de base de datos.

- **Definición**: En un formulario basado en `forms.ModelForm`, defines el modelo que se usará para generar el formulario. Django maneja automáticamente la creación de los campos del formulario basándose en los campos del modelo, así como la validación y el guardado de datos en la base de datos.

- **Ejemplo**:

  ```python
  from django import forms
  from .models import Contact

  class ContactModelForm(forms.ModelForm):
      class Meta:
          model = Contact
          fields = ['customer_email', 'customer_name', 'message']
  ```

- **Uso Típico**: Formularios para crear o editar instancias de modelos en la base de datos, como formularios de contacto, formularios de registro de usuario, o formularios de entrada de datos para una base de datos.

### Diferencias Clave

1. **Vinculación con Modelos**:
   - **`forms.Form`**: No está vinculado a un modelo. Los datos del formulario deben ser procesados manualmente.
   - **`forms.ModelForm`**: Está vinculado a un modelo. Los datos del formulario se guardan automáticamente en el modelo si el formulario es válido.

2. **Generación de Campos**:
   - **`forms.Form`**: Debes definir todos los campos manualmente.
   - **`forms.ModelForm`**: Los campos se generan automáticamente a partir del modelo, aunque puedes personalizar el formulario si es necesario.

3. **Persistencia de Datos**:
   - **`forms.Form`**: No maneja la persistencia de datos; debes implementar el guardado en la base de datos manualmente.
   - **`forms.ModelForm`**: Maneja automáticamente el guardado y la actualización de las instancias del modelo en la base de datos.

4. **Validación**:
   - **`forms.Form`**: Debes definir la lógica de validación manualmente si es necesario.
   - **`forms.ModelForm`**: La validación de los datos es gestionada automáticamente en base a los campos y validaciones definidas en el modelo.

### Cuándo Usar Cada Uno

- **Usa `forms.Form`** cuando necesites formularios para procesos que no están directamente relacionados con modelos de base de datos o cuando quieras más control sobre la validación y procesamiento de datos.

- **Usa `forms.ModelForm`** cuando quieras simplificar la creación de formularios para modelos de Django y necesitas una integración automática entre el formulario y el modelo de base de datos.