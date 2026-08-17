from http import HTTPStatus


def test_root_deve_retornar_ola_mundo(client):
    """
    Teste em 3 etapas (AAA)
    - Arrange
    - Act
    - Assert
    """
    # Arrange - Arranjo

    # Act - Ação
    response = client.get('/')

    # Assert - Garanta
    assert response.json() == {'message': 'Olá mundo!!'}


def test_page_deve_retornar_ola_mundo_html(client):
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


def test_create_user(client):

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
