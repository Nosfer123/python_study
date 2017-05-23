class Wallet:
    def __init__(self, init_amount=0):
        self.init_amount = init_amount
        self.amount = self.init_amount

    def set_income(self, amount):
        self.amount +=amount

    def set_expense(self, amount):
        self.amount -= amount

    def get_amount(self):
        return self.amount

if __name__ == '__main__':
    wallet = Wallet(300)
    assert wallet.get_amount() == 300
    wallet.set_income(200)
    assert wallet.get_amount() == 500
    wallet.set_expense(100)
    assert wallet.get_amount() == 400