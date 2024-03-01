# Contributions Schedule model with id, name, start_date, end_date, amount, frequency
class ContributionsSchedule:
    id: uuid.UUID
    name: str
    start_date: datetime.date
    end_date: datetime.date
    amount: float
    frequency: str

    def __init__(self, name, start_date, end_date, amount, frequency='monthly') -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.amount = amount
        self.frequency = frequency
        pass