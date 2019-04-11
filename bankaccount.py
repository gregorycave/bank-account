
class BankAccount:
  #the init method has two parameter variables:self,bal
  #the bal parameter will accept the accounts starting balance as an argument

  def __init__(self,bal):
    self._balance=bal     #bal is assigned to the objects_balance attribute

  def deposit(self,amount):   #method to make a deposit into account
    self._balance+=amount

  def withdraw(self,amount):    #method to withdraw money from account if in credit
    if self._balance>=amount:
      self._balance-=amount
    else:
      print('Insufficient funds available')

  def get_balance(self):    #the get_balance method returns the account balance
    return self._balance
