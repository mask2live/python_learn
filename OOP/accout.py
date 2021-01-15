
class Account:

    def __init__(self, filepath):
        self.path = filepath
        with open(self.path, 'r') as f:
            self.data = int(f.read())


    def withdraw(self, amount):
        self.data = self.data - amount
        


    def deposit(self, amount):
        self.data = self.data + amount

    
    def commit(self):
        with open(self.path, 'w') as f:
            f.write(str(self.data))

    
    def __str__(self):
        return f"account is {self.data}"

    
class Checking(Account):
    """ Inheritance """

    type = "checking"

    def __init__(self, filepath, fee):
        super().__init__(filepath)
        self.fee = fee

    
    def transfer(self, amount):
        """transfer"""
        self.data = self.data - amount - self.fee



if __name__ == "__main__":

    print("=====Checking=====")
    check = Checking("OOP/data.txt", 3)
    print(check)
    print(check.data)
    check.deposit(check.data)
    check.transfer(100000)
    check.commit()

    print(check.type)
    print(check.transfer.__doc__)


    print("=====Account=====")
    account = Account("OOP/data.txt")
    print(account)
    account.withdraw(50000)
    print(account.data)

    account.deposit(60000)
    print(account.data)

    account.commit()
    