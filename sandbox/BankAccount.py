
class BankAccount:

    __slots__ = ['_number','_holder','_bank','_balance']
    valuta = '€'

    def __init__(self, number, holder, bank = 'unknown'):
        self._number = number
        self._holder = holder
        self._bank = bank
        self._balance = 0

    @property
    def number(self):
        return self._holder

    @property
    def holder(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    @holder.setter
    def set_holder(self, holder):
        self._holder = holder

    @number.setter
    def set_number(self, number):
        self._number = number

    # @balance.setter
    # def set_balance(self, amount):
    #     self._balance = amount

    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
            print(f'Withdrawal of {BankAccount.valuta}{amount}')
        else:
            print('No saldo')

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit of {BankAccount.valuta}{amount}')

    def get_info(self):
        print(f'Bankaccount with number {self._number} belongs to {self._holder} has a saldo of €{self._balance}.')

    @classmethod
    def set_valuta(cls, valuta):
        cls.valuta = valuta


# ------------------------------------------------------------

BankAccount.set_valuta('$')

acc1 = BankAccount('NL54ABCD09876564324', 'Tammaso')

acc1.deposit(1000)
acc1.withdraw(120)
acc1.withdraw(80)

acc1.withdraw(8000)

acc1.get_info()


acc2 = BankAccount('NL54ABCD0976766574', 'Diana')

acc2.deposit(1000)
acc2.withdraw(900)
acc2.withdraw(80)
acc2.withdraw(2)

acc2.get_info()