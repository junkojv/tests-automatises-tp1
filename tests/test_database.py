import pytest

from app.database import Database


@pytest.fixture
def database():
    db = Database()
    db.connect()
    yield db
    db.disconnect()


def test_add_user(database):
    assert database.add_user("alice", "alice@example.com") is True


def test_get_user(database):
    database.add_user("alice", "alice@example.com")

    user = database.get_user("alice")

    assert user == {
        "username": "alice",
        "email": "alice@example.com",
    }


def test_delete_user(database):
    database.add_user("alice", "alice@example.com")

    assert database.delete_user("alice") is True
    assert database.get_user("alice") is None


def test_get_unknown_user(database):
    assert database.get_user("unknown") is None


def test_delete_unknown_user(database):
    assert database.delete_user("unknown") is False


def test_add_duplicate_user(database):
    assert database.add_user("alice", "alice@example.com") is True
    assert database.add_user("alice", "alice@example.com") is False
