from pydantic import BaseModel, constr, ValidationError, validator

class User(BaseModel):
    username: constr(min_length=6, max_length=10)
    password: constr(min_length=8)

    @validator("username")
    def validate_username(cls, value):
        if not value.isalnum():
            raise ValueError("invalid username format!")
        return value

    @validator("password")
    def validate_password(cls, value):
        if not all(char.isalnum() or char in "@#$%&" for char in value):
            raise ValueError("invalid password format!")
        return value
    
class Ping(BaseModel):
    host: str

class Cart(BaseModel):
    card_value: str