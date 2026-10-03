# Agenda Planify

Backend con Django REST Framework que automatiza la elaboración y el seguimiento de planes de trabajo mensuales. Organiza las actividades día por día a partir del documento cargado.

## Qué hace

- **Actividades:** cada actividad tiene nombre, hora, día, mes, responsable, participantes y lugar. El día debe estar entre 1 y 31.
- **Planes mensuales (`ST_Mensual`):** guarda el documento subido de un mes, las actividades asociadas y si ya fue procesado.
- **Planes de trabajo (`Pt_FTL` y `Pt_UCI`):** guardan el archivo de cada plan, el mes y si fue generado.
- Lista y detalle por API para actividades y planes `pt_ftl`.

## Tecnologías

- Python y Django
- Django REST Framework
- SQLite en desarrollo (la configuración de PostgreSQL está comentada en `settings.py`)

## Estructura

```
agenda_planify/             # app principal
  models/                   # Activity, ST_Mensual, Pt_FTL, Pt_UCI
  serializers/              # serializadores
  views/                    # vistas genéricas de DRF
agenda_planify_django/      # configuración del proyecto (settings, urls)
uploads/                    # documentos subidos
agenx.xmi                   # modelo UML exportado
manage.py
```

## Puesta en marcha

1. Crea y activa un entorno virtual.
2. Instala las dependencias: `pip install django djangorestframework`.
3. Genera las migraciones, porque las carpetas `migrations/` no están en el repositorio:

```bash
python manage.py makemigrations agenda_planify
python manage.py migrate
python manage.py runserver
```

## Endpoints

| Ruta | Método | Descripción |
|---|---|---|
| `/activity/` | GET, POST | Lista y crea actividades |
| `/activity/<id>/` | GET, PUT, PATCH, DELETE | Detalle, edición y eliminación de una actividad |
| `/pt_ftl/` | GET, POST | Lista y crea planes de trabajo `pt_ftl` |
| `/pt_ftl/<id>/` | GET, PUT, PATCH, DELETE | Detalle, edición y eliminación de un plan |
| `/admin/` | - | Panel de administración de Django |
