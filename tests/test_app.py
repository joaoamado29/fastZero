from http import HTTPStatus

from fastapi.testclient import TestClient

from fastzero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Teste em 3 etapas (AAA)
    - Arrange
    - Act
    - Assert
    """
    # Arrange - Arranjo
    client = TestClient(app)

    # Act - Ação
    response = client.get('/')

    # Assert - Garanta
    assert response.json() == {'message': 'Olá mundo!!'}


def test_page_deve_retornar_ola_mundo_html():
    client = TestClient(app)
    response = client.get('/page').text
    assert (
        response
        == """
    <html>
        <head>
            <title>Meu App</title>
        </head>
        <body>
            <h1>Olá mundo!!</h1>
        </body>
    </html>
    """
    )


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'username': 'testuser',
            'email': 'teste@email.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testuser',
        'email': 'teste@email.com',
        'id': 1,
    }
