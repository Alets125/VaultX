"""
WSGI config for videogame_catalog project.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videogame_catalog.settings')
application = get_wsgi_application()

# Alias requerido por Vercel para detectar el punto de entrada WSGI
app = application
