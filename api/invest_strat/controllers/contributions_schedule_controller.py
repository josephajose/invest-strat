from models.contributions_schedule import ContributionsSchedule
from db.memory import contributions_schedules

class ContributionsScheduleController:
    def post(self, contributions_schedule: dict):
        # create contributions schedule
        schedule = ContributionsSchedule(
            name=contributions_schedule["name"],
            start_date=contributions_schedule["start_date"],
            end_date=contributions_schedule["end_date"],
            amount=contributions_schedule["amount"],
            frequency=contributions_schedule["frequency"]
        )
        contributions_schedules[schedule.id] = schedule
        return {"message": "Contributions schedule posted"}