from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Literal, List

class PersonalInfo(BaseModel):
    name : str = Field(..., min_length=3, max_length=20, description='This is name')
    age : int | None = Field(..., ge=0, description="This is age")
    # For exemple, no @ sign will throw an error
    email : str = Field(..., description="This is email")

    @field_validator('email', mode='after')
    def email_check(cls, value : str):
        if '@' not in value:
            raise ValueError('Email invalid')
        return value
    

def main():
    Me = PersonalInfo(**{'name' : 'Louis-Antoine', 'age' : 25, 'email' : 'louisantoine.habregmail.com'})


if __name__ == '__main__':
    main() 