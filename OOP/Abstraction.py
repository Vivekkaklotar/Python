from abc import ABC,abstractmethod

class Account(ABC):
    balance = 0
    
    
    @abstractmethod
    def deposit(self,amount):
        pass
    
    @abstractmethod
    def withdraw(self,amount):
        pass
    
# class Saving(Account):
    
#     def deposit(self,amount):
#         self.balance += amount
        
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
            
# s = Saving()
# s.deposit(1000)
# print(s.balance)
# s.withdraw(500)
# print(s.balance)


#loan

class Loan(Account):
    
    def deposit(self,amount):
        if amount>=self.balance:
            t = self.balance - amount
            self.balance = 0
            print(f"Loan cleared, remaining amount: {t}")
        else:
            self.balance -= amount
            
    
            
    def withdraw(self,amount):
        self.balance += amount
        
    def get_balance(self):
        print(f"Balance: {self.balance}")
    
l = Loan()
l.get_balance()
l.withdraw(1000)
l.deposit(500)
l.get_balance()

