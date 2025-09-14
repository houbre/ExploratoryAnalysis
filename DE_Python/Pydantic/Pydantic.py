from pydantic import BaseModel, Field, StrictInt

class input(BaseModel):

    # Validation
    x : StrictInt = Field(..., description="This is x")
    y : str = Field(default="Louis", description="This is y")



def SomeFct(param:input):
    print("Hello Haber")

def main():
    #this will also work because pydantic converts the str into int
    #pyd_input = input(x="10", y="Hello There")

    pyd_input = input(**{"x":10})

    SomeFct(pyd_input)


if __name__ == '__main__':
    main()

