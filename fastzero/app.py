from http import HTTPStatus

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastzero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

database = []  # Simulação de um banco de dados em memória

app = FastAPI()


# Endpoint para retornar uma mensagem JSON
@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo!!'}


# Endpoint para retornar uma página HTML
@app.get('/page', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_page():
    return """
    <html>
        <head>
            <title>Meu App</title>
        </head>
        <body>
            <h1>Olá mundo!!</h1>
        </body>
    </html>
    """


# Criar
@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


# Pegar
@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


# Pegar por id
@app.get(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def search_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado!'
        )

    return database[user_id - 1]


# Atualizar
@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Usuário não encontrado!'
        )
    database[user_id - 1]

    return user_with_id


# Delete
@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado!',
        )
    return database.pop(user_id - 1)
