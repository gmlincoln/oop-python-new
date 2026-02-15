class Bank:

    def __init__(self, balance):
        self.balance = balance 
        self.__balance = balance   # private variable

    def show_balance(self):
        return self.__balance
    
    
    
    
bank_obj = Bank(4000)
print(bank_obj.balance)
# print(bank_obj.__balance)
print(bank_obj.show_balance())

# b = Bank(5000)
# print(b.balance)



