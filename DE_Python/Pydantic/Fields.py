from pydantic import BaseModel, Field, EmailStr
from typing import Literal, List

class personal_info(BaseModel):
    name : str = Field(..., min_length=3, max_length=20, description='This is name')
    age : int | None = Field(..., ge=0, description="This is age")
    # For exemple, no @ sign will throw an error
    email : EmailStr = Field(..., description="This is email")
    gender : Literal["male", "female", "other"] = Field(..., description="this is gender")
    salaries : List[int] = Field(..., description="this is salaries")


def PrintPersonalInfo(person:personal_info):
    print(person.name)
    print(person.age)
    print(person.email)
    print(person.gender)
    print(person.salaries)


def main():
    Me = personal_info(**{"name" : "Louis-Antoine", "age" : 25, "email" : "louisantoine@hotmail.com", "gender" : "male", "salaries" : [100000, 5000000]})
    PrintPersonalInfo(Me)

if __name__ == '__main__':
    main()