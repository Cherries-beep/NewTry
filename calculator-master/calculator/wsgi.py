

import os
import sys

# Добавляем путь к проекту
sys.path.append('/Users/viktoriavlasova/PycharmProjects/GeoCalc/calculator-master')

# Указываем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calculator.settings')

# Импортируем WSGI-приложение
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


