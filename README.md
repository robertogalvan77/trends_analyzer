# Trends Analyzer

Trends Analyzer es una aplicación web desarrollada con Django que muestra las tendencias actuales de búsqueda en Google y YouTube utilizando la API de Google Trends.

## Requisitos

- Python 3.x
- Django 4.2.20
- pytrends (para consultar Google Trends)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/trends_analyzer.git
   cd trends_analyzer

2. Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Windows usa 'venv\Scripts\activate'


3. Instala las dependencias:

pip install -r requirements.txt

4. Configura la base de datos:
python manage.py migrate

5. Runserver
python manage.py runserver

Uso

    /google/: Muestra las tendencias de búsqueda de Google.

    /youtube/: Muestra las tendencias de búsqueda de YouTube.

Contribuir

    Haz un fork de este repositorio.

    Crea una nueva rama (git checkout -b feature/nueva-caracteristica).

    Haz tus cambios y haz commit.

    Empuja tus cambios a tu fork.

    Abre un pull request para que revisemos tus cambios.
