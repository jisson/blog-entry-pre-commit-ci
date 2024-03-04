from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.models import TimeStampedModel

from .constants import EntryStatusChoices

User = get_user_model()


class Entry(TimeStampedModel):

    title = models.CharField(max_length=200)
    content = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.IntegerField(
        choices=EntryStatusChoices, default=EntryStatusChoices.DRAFT
    )
