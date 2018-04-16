# -*- coding: utf-8 -*-
"""
WSGI config for project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lazydoc.settings')

project_path = os.path.realpath(os.path.dirname(__file__))
paths = []
paths.append(project_path)
paths.append(os.path.dirname(project_path))
paths.append(os.path.dirname(os.path.dirname(project_path)))

for path in paths:
    if path not in sys.path:
        sys.path.append(path)

application = get_wsgi_application()
