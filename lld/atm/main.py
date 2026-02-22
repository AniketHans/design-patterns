from enum import Enum
import threading
import uuid


class Notes:
    NOTE_100 = "100"
    NOTE_500 = "500"
    NOTE_2000 = "2000"

class Account:
    def __init__(self, balance):
        self.account_id = str(uuid.uuid4())[:6]
        self.balance = balance
    def add_money(self, amount):
        self.balance+= amount
    def debit_money(self, amount):
        if self.balance<amount:
            raise Exception("Insufficient Balance")
        self.balance -= amount

class Bank:
    def __init__(self):
        self.bank_id = str(uuid.uuid4())[:6]
        self.accounts = {}
    def add_account(self, account: Account):
        self.accounts[account.account_id] = account
    def getAccount(self, account_id):
        if account_id not in self.accounts:
            raise Exception("Not account exists with the given id")
        return self.accounts[account_id]

class CashInventory:
    def __init__(self):
        self.notes = {
            Notes.NOTE_100:  0,
            Notes.NOTE_500:  0,
            Notes.NOTE_2000: 0 
        }
        self.lock = threading.Lock()
    def addNotes(self, note: str, qty:int):
        self.notes[note]+=qty
        
    def canDispense(self, amount):
        notesSorted = sorted(list(map(lambda x: int(x), self.notes.keys())),reverse=True)
        n = len(notesSorted)
        i=0
        while i<n and amount!=0:
            p = notesSorted[i]
            q = amount // p
            if q <= self.notes[str(notesSorted[i])]:
                amount = amount % p
            i+=1
        return amount==0

    def dispenseCash(self, amount):
        with self.lock:
            if not self.canDispense(amount):
                raise Exception("Insufficient cash!!")
            notesSorted = sorted(list(map(lambda x: int(x), self.notes.keys())),reverse=True)
            n = len(notesSorted)
            i=0
            dispensedNotes = dict()
            while i<n and amount!=0:
                p = int(notesSorted[i])
                q = amount // p
                if q <= self.notes[str(notesSorted[i])]:
                    self.notes[str(notesSorted[i])] -= q
                    dispensedNotes[str(notesSorted[i])] = q
                    amount = amount % p
                i+=1
            return dispensedNotes
        
                
class ATM:
    def __init__(self):
        self.atm_id = str(uuid.uuid4())[:6]
        self.cashInventory = CashInventory()
    
    def withdraw(self, account: Account, amount: int):
        if amount % 100 != 0:
            raise Exception("The amount should be in multiples of 100")
        account.debit_money(amount)
        cash = self.cashInventory.dispenseCash(amount)
        return cash


class ATMService:
    def __init__(self):
        self.atms: dict[str, ATM] = dict()
        self.bank = Bank()
    def add_atms(self, atm: ATM):
        self.atms[atm.atm_id] = atm

    def withrawMoney(self, atm_id, account_id, amount):
        if atm_id not in self.atms:
            raise Exception("ATM not found")
        account = self.bank.getAccount(account_id)
        atm = self.atms[atm_id]
        money = atm.withdraw(account, amount)
        return money

if __name__ == "__main__":
    atm_svc = ATMService()
    
    atm1 = ATM()
    atm1.cashInventory.addNotes(Notes.NOTE_100, 100)
    atm1.cashInventory.addNotes(Notes.NOTE_500, 50)
    atm1.cashInventory.addNotes(Notes.NOTE_2000, 20)
    atm_svc.add_atms(atm1)
    
    account = Account(10000)
    atm_svc.bank.add_account(account)
    
    cash = atm_svc.withrawMoney(atm1.atm_id, account.account_id, 5000)
    print("Cash withdrawn:", cash)
    print("Remaining Balance:", account.balance)
    
    
    
    
    