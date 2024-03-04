import os

from .base import *  # noqa: F403,F401

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-p^)f*d_$4g)ik!-tbi#4!j=mda-%l-dj^sb@d(vx#roj%rk1(c",
)
DEBUG = True
