from pydantic import BaseModel
from enum import Enum

upper_level = ("Управління",
               "1 Рота",
               "2 рота",
               "3 рота")

mid_level = ("1 взвод",
             "2 взвод",
             "3 взвод")


class FullName(BaseModel):
    first_name: str
    surname: str
    last_name: str

class SalaryIndex():
    int(range[0:50])
class Position(BaseModel):
    position_name: str
    salary_index: SalaryIndex
    upper_level: str in upper_level
    mid_level: str in mid_level | None
    low_level: str

position = Position(
    "Комбат",
    "12",
    "Управління",
    None,
    "хуй"
)

print(position)