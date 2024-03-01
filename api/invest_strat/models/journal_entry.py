import uuid
import datetime

# JournalEntry model with id, date, amount
class JournalEntry:
    id: uuid.UUID
    date: datetime.date
    amount: float

    def __init__(self, date, amount) -> None:
        self.id = uuid.uuid4()
        self.date = date
        self.amount = amount
        pass