from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastzero.schemas import Message, UserDB, UserPublic, UserSchema

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


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id
