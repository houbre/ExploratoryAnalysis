from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import Literal, List


class input(BaseModel):
    query : str = Field(..., description="input query")

class output(BaseModel):
    query : str = Field(..., description="input query")
    result : str = Field(..., description="input query")


def process_data(p_input: input) -> output:

    input_query = p_input.query
    some_result = "Hello!"

    Output = output(query=input_query, result=some_result)

    return Output

    

def main():
    input_query = input(query="yooo")
    result = process_data(input_query)
    
    print(result)

    print('-------------')

    # Convert to dictionnary
    print(result.model_dump())

    print('-------------')

    # Convert to json
    print(result.model_dump_json())


if __name__ == '__main__':
    main() 