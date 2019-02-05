#Necessary for native django server run testing

import os
import django
from channels.routing import get_default_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatter.settings")
django.setup()
application = get_default_application()