from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import Literal, List


class order(BaseModel):
    id : int = Field(..., description="id")
    price_per_unit : int = Field(..., description="price per unit")
    units : int = Field(..., description="units")


    @computed_field
    @property
    def total_price(self) -> int:
        return self.price_per_unit * self.units
    

def main():
    Order = order(id=555, price_per_unit=5, units=20)
    print(Order)


if __name__ == '__main__':
    main() 