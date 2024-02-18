from models.account import Account
from models.account_entry import AccountEntry
from models.journal_entry import JournalEntry
from db.memory import *

class JournalEntryController:
    
    def get(self):
        # expand account entries for each journal entry
        all_journal_entries = []
        for journal_entry in journal_entries.values():
            journal_entry_dict = vars(journal_entry).copy()
            journal_entry_dict["account_entries"] = []
            for account_entry in account_entries.values():
                if account_entry.journal_entry == journal_entry.id:
                    account_entry_dict = vars(account_entry).copy()
                    account_entry_dict["account"] = vars(accounts[account_entry.account])
                    journal_entry_dict["account_entries"].append(account_entry_dict)
            all_journal_entries.append(journal_entry_dict)
        return all_journal_entries
    
    def post(self, journal_entry: dict):
        # create journal entry
        entry = JournalEntry(
            date=journal_entry["date"],
            amount=journal_entry["amount"]
        )
        journal_entries[entry.id] = entry

        # create account entries
        for account_entry in journal_entry["account_entries"]:
            account = None
            for acc in accounts.values():
                if acc.name == account_entry["account"]:
                    account = acc
                    break
            if not account:   
                account = Account(
                    name=account_entry["account"]
                )
                accounts[account.id] = account
            
            # create account entry
            new_account_entry = AccountEntry(
                account=account.id,
                journal_entry=entry.id,
                date=entry.date,
                type=account_entry["type"],
                amount=entry.amount,
            )
            account_entries[new_account_entry.id] = new_account_entry

        return {"message": "Journal entry posted"}
