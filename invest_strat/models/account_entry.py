import uuid
import datetime

# AcountEntry model with id, account, journal_entry, date, amount
class AccountEntry:
    id: uuid.UUID
    account: uuid.UUID
    journal_entry: uuid.UUID
    date: datetime.date
    type: str
    amount: float

    def __init__(self, account, journal_entry, date, type, amount) -> None:
        self.id = uuid.uuid4()
        self.account = account
        self.journal_entry = journal_entry
        self.date = date
        self.type = type
        self.amount = amount
        pass
