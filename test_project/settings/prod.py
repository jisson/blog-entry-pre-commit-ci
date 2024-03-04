import os

from .base import *  # noqa: F403,F401

# Secret key is mandatory in production.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = False
