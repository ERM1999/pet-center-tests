# PetCenter Automation Framework

Framework de pruebas automatizadas diseñado para validar el flujo completo de la aplicación **PetCenter Web** mediante pruebas funcionales end-to-end.

## Funcionalidad del Proyecto

El framework permite automatizar la validación de los principales procesos de negocio de la aplicación:

* **Mascotas:** Validación completa del flujo de creación, búsqueda y verificación de datos.
* **Adopciones:** Automatización de los procesos críticos relacionados con los pedidos de adopción.
* **Usuarios:** Comprobación de los flujos principales de gestión y administración de usuarios.

> **Nota técnica:** El framework sigue una arquitectura basada en Page Object Model (POM), permitiendo desacoplar la lógica de automatización de la estructura visual de la aplicación y facilitando el mantenimiento de las pruebas.


## Tecnologías

* Python 3
* Behave (BDD)
* Selenium WebDriver
* Page Object Model (POM)

## Estructura del Framework

### features/

Archivos `.feature` escritos en Gherkin que describen los escenarios de prueba desde la perspectiva del usuario.

### steps/

Implementación en Python de los pasos definidos en los escenarios.

### page_objects/

Componentes que encapsulan los elementos y acciones de cada página para mejorar la reutilización y el mantenimiento.

### utils/

Funciones auxiliares y configuraciones compartidas entre los distintos módulos del framework.

## Configuración del Entorno

Asegúrate de tener instalado Python 3 en tu equipo.

### Crear entorno virtual

```bash
python -m venv venv
```

### Activar entorno virtual

```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

Para ejecutar el conjunto completo de pruebas:

```bash
behave
```

---

*Framework de pruebas desarrollado como parte de un plan de aprendizaje continuo en automatización, calidad de software y testing end-to-end para la plataforma PetCenter.*
