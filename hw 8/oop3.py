#Q1: write the Circle class according to the specifications below:
import math
class Circle():
 def __init__(self):
 # initilizes self with radius
  self.radius = None
 def get_radius(self):
 # returns radius of self
  return self.radius
 def set_radius(self, radius):
 # changes the radius attribute of self to radius
  self.radius = radius
 def area(self):
 # computes and returns area of self
  return (self.radius ** 2) * math.pi
 def __eq__(self, other):
 # other is a Circle object
 # returns True if self and other has the same radius value
  if self.radius == other.radius :
      return True
  else:
      return False
 def __gt__(self, other):
 # other is a Circle object
 # returns self or other, Circle object with the bigger radius
  if self.radius > other.radius :
      return self
  elif self.radius < other.radius :
      return other
  else :
      return f'both cicle have same radius'
 
 def __add__(self, other):
 # other is a Circle object
 # returns a new Circle object that it's radius is
 # the sum of self and other's radius
  sum_circle = Circle()
  sum_circle.radius = self.radius + other.radius
  return sum_circle
 def __str__(self):
 # a Circle's string reperesentation is the radius
  return f'circle radius : {self.radius}'

#Q2: Create a BankAccount class with the following three types of attributes:
class BankAccount():
    def __init__(self,account_holder):
        self.account_holder = account_holder
        self.__balance = 0
        self._transaction_history = []
    def deposit(self,amount):
        self.__balance += amount
        self._transaction_history.append(f'deposit ${amount}')
    def withdraw(self,amount):
        if self.__balance >= amount :
           self.__balance -= amount
           self._transaction_history.append(f'withdraw ${amount}')
           return self.__balance
        else:
            raise ValueError("Insufficient funds!")
    @property
    def check_balance(self):
        return self.__balance
    def show_history(self):
        for i in self._transaction_history:
            print(i)
    
account = BankAccount("John")
# Test all methods
account.check_balance # Balance: $0
account.deposit(100) # Deposited $100
account.withdraw(30) # Withdrew $30
account.withdraw(100) # Insufficient funds!
account.check_balance() # Balance: $70
account.show_history()
class SavingsAccount(BankAccount):
    def show_transactions(self):
        for t in self._transaction_history:
            print(t)
