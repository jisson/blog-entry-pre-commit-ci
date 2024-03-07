import factory
from django.contrib.auth import get_user_model
from factory import fuzzy

from .models import Entry

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = "john"
    password = factory.django.Password("password")


class EntryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry

    title = fuzzy.FuzzyText(length=200)
    content = fuzzy.FuzzyText(length=2000)

    author = factory.SubFactory(UserFactory)
