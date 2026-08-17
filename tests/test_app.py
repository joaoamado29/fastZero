from http import HTTPStatus


##########################################
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


##########################################
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


##########################################
def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'joao',
            'email': 'joao@email.com',
            'password': 'testpassword',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'joao',
        'email': 'joao@email.com',
        'id': 1,
    }


##########################################
def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'joao',
                'email': 'joao@email.com',
                'id': 1,
            }
        ]
    }


##########################################
def test_search_users(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'joao',
        'email': 'joao@email.com',
        'id': 1,
    }

    # Teste do tratamento de erro
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND


##########################################
def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }

    # Teste do tratamento de erro
    response = client.put(
        '/users/2',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND


##########################################
def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'joao',
        'email': 'joao@email.com',
        'id': 1,
    }

    # Teste do tratamento de erro
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
