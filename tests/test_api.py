import pytest

from app import create_app
from app import api as api_module


@pytest.fixture
def app(tmp_path):
    database_path = tmp_path / "test_api.db"
    app = create_app({
        "TESTING": True,
        "DATABASE": str(database_path),
    })
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_index_route(client):
    response = client.get("/")

    assert response.status_code == 200
    assert "L'application fonctionne" in response.get_data(as_text=True)


def test_api_test_endpoint(client):
    response = client.get("/api/test")

    assert response.status_code == 200
    assert response.get_json() == {"status": "API fonctionne correctement"}


def test_add_endpoint(client):
    response = client.get("/api/add/2/3")

    assert response.status_code == 200
    assert response.get_json() == {"result": 5.0}


def test_divide_by_zero_endpoint(client):
    response = client.get("/api/divide/10/0")

    assert response.status_code == 400
    assert response.get_json() == {"error": "Division par zéro impossible"}


def test_invalid_number_endpoint(client):
    response = client.get("/api/add/a/3")

    assert response.status_code == 400
    assert response.get_json() == {"error": "Les paramètres doivent être des nombres"}


def test_add_user_endpoint(client):
    response = client.post(
        "/api/user",
        json={"username": "alice", "email": "alice@example.com"},
    )

    assert response.status_code == 201
    assert response.get_json() == {"message": "Utilisateur ajouté avec succès"}


def test_get_user_endpoint(client):
    client.post(
        "/api/user",
        json={"username": "alice", "email": "alice@example.com"},
    )

    response = client.get("/api/user/alice")

    assert response.status_code == 200
    assert response.get_json() == {
        "username": "alice",
        "email": "alice@example.com",
    }


def test_delete_user_endpoint(client):
    client.post(
        "/api/user",
        json={"username": "alice", "email": "alice@example.com"},
    )

    response = client.delete("/api/user/alice")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Utilisateur supprimé avec succès"}


def test_add_user_with_missing_fields(client):
    response = client.post(
        "/api/user",
        json={"username": "alice"},
    )

    assert response.status_code == 400
    assert response.get_json() == {"error": "Les champs username et email sont requis"}


def test_get_unknown_user_endpoint(client):
    response = client.get("/api/user/unknown")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Utilisateur non trouvé"}


def test_add_duplicate_user_endpoint(client):
    client.post(
        "/api/user",
        json={"username": "alice", "email": "alice@example.com"},
    )

    response = client.post(
        "/api/user",
        json={"username": "alice", "email": "alice@example.com"},
    )

    assert response.status_code == 409
    assert response.get_json() == {"error": "Cet utilisateur existe déjà"}


def test_delete_unknown_user_endpoint(client):
    response = client.delete("/api/user/unknown")

    assert response.status_code == 404
    assert response.get_json() == {"error": "Utilisateur non trouvé"}


def test_add_user_endpoint_with_mocked_database(client, mocker):
    mocked_db = mocker.Mock()
    mocked_db.add_user.return_value = True
    mocker.patch.object(api_module, "db", mocked_db)

    response = client.post(
        "/api/user",
        json={"username": "bob", "email": "bob@example.com"},
    )

    assert response.status_code == 201
    assert response.get_json() == {"message": "Utilisateur ajouté avec succès"}
    mocked_db.add_user.assert_called_once_with("bob", "bob@example.com")
