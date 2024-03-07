import pytest

from test_project.apps.core.factories import EntryFactory, UserFactory


@pytest.mark.django_db
def test_model_user():
    """
    Dumb test. Only here to demonstrate the configuration of bandit in pre-commit hooks.
    """
    author = UserFactory(username="john", password="test_password")
    entry = EntryFactory(author=author)

    assert entry.author.id == author.id
