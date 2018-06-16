class Value(object):
    def __get__(self, instance, owner):
        return int(self.value - (self.value*instance.commission))

    def __set__(self, instance, value):
        self.value = value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)