from django.db import models


# Models constants
# ------------------------------------------------------------------------------
class EntryStatusChoices(models.IntegerChoices):
    DRAFT = 1
    PUBLISHED = 2
    ARCHIVED = 3
