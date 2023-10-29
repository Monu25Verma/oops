# import random

# class Acount:
#     print(" Welcome to banking portal! ")

# class New_Acount:
#     def __init__(self, name, inital_deposit):
#         self.name = name
#         self.inital_deposit = inital_deposit

#     def generate_account(self):
#         n = 5
#         Acc_create = int(''.join(str(random.randint(0,9)) for _ in range(n)))
#         print("New user account created successfully and Account number is:", Acc_create)

# class ExistingAccount:
#     def __init__(self, name, accountNo):
#         self.name = name
#         self.accountNo = accountNo
    
#     def choices(self):
#         while True:
#             print("enter 1 to withdraw")
#             print("enter 2 to deposit")
#             print("enter 3 to display")
#             print("enter 4 to exit")

#             userchoice  = int(input("Enter your choice: "))
#             print()

#             if userchoice == 1:
#                 account.availablebook()
#                 print()
#             elif userchoice == 2:
#                 account.lendbook(input("Enter Book Name:"))
#                 print()
#             elif userchoice == 3:
#                 account.addbook(input("Enter Book Name to Add:"))
#                 print()
#             elif userchoice == 4:
#                 quit()


# if __name__ == '__main__':
#     # existing_acc = ExistingAccount()
#     # existing_acc.
#     # account = ExistingAccount(["withdraw" , "deposit", "display", "exit"])
    
        
from random import randint
from abc import ABCMeta ,abstractmethod
class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    
    @abstractmethod
    def Authentication():
        return 0

    @abstractmethod
    def withdraw():
        return 0
    
    @abstractmethod
    def Deposite():
        return 0
    
    @abstractmethod
    def DisplayBalance():
        return 0
class ExistingAccount(Account):
    def __init__(self):
        self.exisitngAccounts = {}
    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.exisitngAccounts[self.accountNumber] = [name, initialDeposit]
        print("Acount created sucesfully. your account number is ", self.accountNumber)
    
    def Authentication(self, name, accountNumber):
        if accountNumber in self.exisitngAccounts.keys():
            if self.exisitngAccounts[accountNumber][0] == name:
                print("Authentication Successfull")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication fail")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdraw(self, withdrawAmmount):
        if withdrawAmmount > self.exisitngAccounts[self.accountNumber][1]:
            print("Insufficent balance")
        else:
            self.exisitngAccounts[self.accountNumber][1] -= withdrawAmmount
            print("withdrawal was successful.")
            self.DisplayBalance()

    def Deposite(self, DepositAmount):
        self.exisitngAccounts[self.accountNumber][1] += DepositAmount
        print("Account Deposited Successfully.")
        self.DisplayBalance()


    def DisplayBalance(self):
        print("Available balance are ", self.exisitngAccounts[self.accountNumber][1])


exixting_Acount = ExistingAccount()
while True:
    print("enter 1 for new account")
    print("enter 2 for Exisiting Account")
    print("enter 3 to exit")
    userchoice = int(input())
    if userchoice is 1:
        print("Enter your name: ")
        name = input()
        print("enter initial deposite")
        initialDeposit = int(input())
        exixting_Acount.createAccount(name, initialDeposit)
    elif userchoice is 2:
        print("enter the name: ")
        name = input()
        print("Enter the your Account number: ")
        accountNumber = int(input())
        authenticatestatus = exixting_Acount.Authentication(name, accountNumber)
        if authenticatestatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposite")
                print("Enter 3 to display amount")
                print("Enter 4 to back to previous")
                userchoice = int(input())
                if userchoice is 1:
                    print("Enter a withdraw amount")
                    withdrawAmmount = int(input())
                    exixting_Acount.withdraw(withdrawAmmount)
                
                elif userchoice is 2:
                    print("Enter a deposit amount")
                    DepositAmount = int(input())
                    exixting_Acount.Deposite(DepositAmount)

                elif userchoice is 3:
                    exixting_Acount.DisplayBalance()

                elif userchoice is 4:
                    break
            
        elif userchoice is 3:
            quit()






