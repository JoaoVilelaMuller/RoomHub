import pytest

from app import create_app


@pytest.fixture
def client(tmp_path):
    app = create_app(f"sqlite:///{tmp_path / 'roomhub_test.db'}")
    app.config.update(TESTING=True)
    with app.test_client() as test_client:
        yield test_client


def test_usuario_crud_and_password_is_not_returned(client):
    created = client.post(
        "/api/usuarios",
        json={
            "nome": "João",
            "email": "joao@example.com",
            "senha": "segredo",
            "tipo_usuario": "estudante",
        },
    )

    assert created.status_code == 201
    user = created.get_json()
    assert user["id"] == 1
    assert "senha" not in user

    fetched = client.get(f"/api/usuarios/{user['id']}")
    assert fetched.status_code == 200
    assert fetched.get_json()["email"] == "joao@example.com"

    updated = client.put(
        f"/api/usuarios/{user['id']}",
        json={
            "nome": "João Atualizado",
            "email": "joao@example.com",
            "senha": "segredo",
            "tipo_usuario": "estudante",
        },
    )
    assert updated.status_code == 200
    assert updated.get_json()["nome"] == "João Atualizado"

    deleted = client.delete(f"/api/usuarios/{user['id']}")
    assert deleted.status_code == 200
    assert client.get(f"/api/usuarios/{user['id']}").status_code == 404


def test_usuario_validation_and_duplicate_email(client):
    payload = {
        "nome": "João",
        "email": "joao@example.com",
        "senha": "segredo",
        "tipo_usuario": "estudante",
    }
    assert client.post("/api/usuarios", json={}).status_code == 400
    assert client.post("/api/usuarios", json=payload).status_code == 201
    duplicate = client.post("/api/usuarios", json=payload)
    assert duplicate.status_code == 409


def test_moradia_crud_and_invalid_price(client):
    invalid = client.post(
        "/api/moradias",
        json={
            "titulo": "República",
            "cidade": "Campinas",
            "universidade": "Unicamp",
            "preco": -1,
        },
    )
    assert invalid.status_code == 400

    created = client.post(
        "/api/moradias",
        json={
            "titulo": "República",
            "descricao": "Perto da universidade",
            "cidade": "Campinas",
            "universidade": "Unicamp",
            "preco": 700,
        },
    )
    assert created.status_code == 201
    moradia = created.get_json()
    assert moradia["id"] == 1

    updated = client.put(
        f"/api/moradias/{moradia['id']}",
        json={
            "titulo": "República atualizada",
            "descricao": "Perto da universidade",
            "cidade": "Campinas",
            "universidade": "Unicamp",
            "preco": 750,
        },
    )
    assert updated.status_code == 200
    assert updated.get_json()["preco"] == 750

    assert client.delete(f"/api/moradias/{moradia['id']}").status_code == 200


def test_missing_moradia_returns_404(client):
    assert client.get("/api/moradias/999").status_code == 404