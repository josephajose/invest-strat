import uuid

# Account model with id, name, category, subcategory
class Account:
    id: uuid.UUID
    name: str 
    category: str
    subcategory: str

    def __init__(self, name, category="", subcategory="") -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.category = category 
        self.subcategory = subcategory
        pass
