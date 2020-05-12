'''Your assignment this week you will build a CheckingAccount class and associated driver application.  The class should contain appropriate attributes that you would find in a normal checking account:  name, address, accounts number, balance, etc
The balance should be "private" to the class since it should only be changed through appropriate debit/credit methods.  Recall, you can simulate the private aspect using the _ character at the start of the variable name. 
The class should be saved in a file called CheckingAccount.py
Build a driver application that instantiates a CheckingAccount object and performs a variety of debits and credits as well as prints the balance as appropriate.
'''

class CheckingAccount:
    def __init__(self, name, address, account_num, balance):
        self.name = name
        self.address = address
        self.account_num = account_num
        self._balance = balance

    def __str__(self):
        return f'{self.name}, {self.address}, Account No: {self.account_num}, Balance: ${self._balance:.2f}'

    def withdrawal(self, amount):
        if self._balance - amount > 0:
            self._balance -= amount
            print( f'${amount:.2f} has been subtracted from account. New balance is: ${self._balance:.2f}')
            return self._balance
        else:
            if amount > self._balance:
                print("\n Insufficient balance  ") 
    

    def deposit(self, amount):
        self._balance += amount
        print (f'${amount:.2f} has been added to account. New balance is: ${self._balance:.2f}')
        return self._balance

# Driver application that instantiates a CheckingAccount object and performs a variety of action
def main(): # ATM Transction
    owner = CheckingAccount('Cash Money', 'The Vault', 'xxx999', 1000)
   
    print("Welcome to the Deposit & Withdrawal ATM Machine!") 
    
    while True:
        # enter command
        print('Would you like to: ')
        command = input('(b) Check Account Balance (w) Withdraw Funds, (d) Deposit funds (e) End Transaction ').lower()
        
        # select b, print available balance
        if command == 'b':
            print(f'Available balance: ${owner._balance:.2f} \n')
            
        # select w, ask withdrawal amount subtract from current balance and print available balance
        elif command == 'w':
            amount = float(input('How much would you like to withdraw? $'))
            owner.withdrawal(amount)
            print(f'Available balance: ${owner._balance:.2f} \n')
            
        # select b, ask deposit amount add to current balance and print available balance
        elif command == 'd':
            amount = float(input('How much would you like to deposit? $'))
            owner.deposit(amount)
            print(f'Available balance: ${owner._balance:.2f} \n')
            
        # select e, exit
        elif command == 'e':
            print('Thank you, Goodbye.')
            break
        
        # error message, invalid input
        else:
            print('Invalid input.')

main()