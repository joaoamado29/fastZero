from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastzero.schemas import Message, UserSchema, UserPublicSchema

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

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(user: 'UserSchema'):
    return user