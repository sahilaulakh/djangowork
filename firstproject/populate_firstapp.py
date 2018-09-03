import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","firstproject.settings")

import django
django.setup()

import random
from firstapp.models import Topic, AccessRecord, WebPage