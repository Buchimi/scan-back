from dataclasses import dataclass

@dataclass
class recept_item:
    name: str
    id: int
    price: float
    
# pydantic json into class
# benie 