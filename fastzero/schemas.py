from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserPublicSchema(BaseModel):
    username: str
    email: EmailStr