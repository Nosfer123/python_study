from datetime import datetime
from lesson_9_wallet import Wallet
from lesson_9_bag import AppleBag


class Person:
    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year

    @staticmethod
    def _get_current_year():
        return datetime.now().year

    def get_age(self):
        return self._get_current_year() - self.birth_year

    def is_allowed(self):
        return self.get_age() >= 18


class Trader(Person):
    def __init__(self, wallet, bag, name, gender, birth_year):
        self.wallet = wallet
        self.bag = bag
        super().__init__(name, gender, birth_year)

if __name__ == '__main__':
    wallet = Wallet(100)
    bag = AppleBag(100)
    trader = Trader(wallet, bag, 'Tom', 'M', 1992)

    assert trader.bag.get_amount() == 100
