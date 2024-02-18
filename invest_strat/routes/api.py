from fastapi import APIRouter
from models.account import Account
from models.account_entry import AccountEntry
from models.journal_entry import JournalEntry
from controllers.journal_entry_controller import JournalEntryController
from db.memory import *

router = APIRouter(
    prefix="/api"
)

@router.get("/accounts")
async def get_accounts():
    return list(accounts.values())

@router.get("/account_entries")
async def get_account_entries():
    return list(account_entries.values())

@router.get("/journal_entries")
async def get_journal_entries():
    return JournalEntryController().get()

@router.post("/journal_entries")
async def post_journal_entries(journal_entry: dict):
    return JournalEntryController().post(journal_entry)

@router.post("/contributions/schedules")
async def post_contributions_schedules(contributions_schedule: dict):
    return ContributionShceduleController().post(contributions_schedule)