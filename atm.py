import random as rd
class Bank:
    def __init__(self,username,userac,password,balance):
        self.username = username
        self.userac = userac
        self.password = password
        self.balance = balance
    def otp(self):
        return rd.randint(100000, 999999)
    def bal(self):
        o = self.otp()
        print("Generated OTP :",o)
        a = int(input("Enter the OTP : "))
        if a == o:
            print(f"Available balance  = {self.balance}")
        else:
            print("Enter valid OTP !")
    def withdrawl(self,amt):
        o = self.otp()
        print("Generated OTP :",o)
        a = int(input("Enter the OTP : "))
        if a == o:
            if amt > self.balance:
                print("Insufficient balance !")
            else:
                self.balance = self.balance - amt
                print("Withdrawl Successful !")
                print("Balance : ",self.balance)
        else:
            print("Enter valid OTP !")
    def deposit(self,amt):
        o = self.otp()
        print("Generated OTP :",o)
        a = int(input("Enter the OTP : "))
        if a == o:
            self.balance = self.balance + amt
            print("Money deposited successfully !")
            print("Balance : ",self.balance)
        else:
            print("Enter valid OTP !")
un = input("Enter user name : ")
ac = int(input("Enter account Number : "))
pwd = input("Enter the password : ")
bl = int(input("Enter the balance : "))
ob = Bank(un,ac,pwd,bl)
print("-----------Welcome to e-ATM------------")
while True:
    print("Enter the below number to proceed further ")
    print("1.Balance")
    print("2.Withdrawl")
    print("3.Deposit")
    print("4.Exit")
    n = int(input("Enter the input : "))
    if n==1:
        ob.bal()
        print(" ")
    elif n==2:
        amt = int(input("Enter the amount you want to withdraw : "))
        ob.withdrawl(amt)
        print(" ")
    elif n==3:
        amt = int(input("Enter the amount you want to deposit : "))
        ob.deposit(amt)
        print(" ")
    elif n==4:
        print("Thank you for using e-Atm")
        print("Please use again !")
        print("Have a safe and secure transaction !")
        break
    else:
        print("Enter the correct input")
        print(" ")
