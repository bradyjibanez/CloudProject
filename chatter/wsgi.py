#What is used to reference straight http calls (not for async
#or websockets). Only needed for native django server run testing

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatter.settings')

application = get_wsgi_application()
