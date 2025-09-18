from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import Literal, List


class Api_Auth(BaseModel):
    email : str = Field(..., description="email")
    password : str = Field(..., description="password")
    confirm_password : str = Field(..., description="confirm password")


    @model_validator(mode='after')
    def password_check(cls, values):
        if (values.password != values.confirm_password):
            raise ValueError('Password Not matching')
        return values
    

def main():
    Me = Api_Auth(email='louisantoine.habregmail.com', password='hahaha', confirm_password='hahaha2')
    print('Welcome!')


if __name__ == '__main__':
    main() 