import bankaccount

def main():
  #get start balance from user
  start_bal= float(input('Enter your starting balance: '))
  
  #create bank account object
  savings=bankaccount.BankAccount(start_bal)

  #deposit the users paycheck
  pay=float(input('How much did you get paid?: '))
  print('Depositing {0:.2f} into your account'.format(pay))
  savings.deposit(pay)

  #display the balance
  print('Your account balance is {0:.2f}'.format(savings.get_balance(),sep=''))

  #get the amount to withdraw
  cash=float(input('How much would you like to withdraw? :'))
  print('Withdrawing from account...')
  savings.withdraw(cash)

  #display the balance
  print('Your account balance is {0:.2f}'.format(savings.get_balance(),sep=''))

main()
