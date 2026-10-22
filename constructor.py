# class company:
#     name="MindDMC"
#     location="Noida"
                     
#     def __init__ (self):
#         print(f"Company Details : Name : {self.name}, Location : {self.location}")    
               
# x=company()


class BankAccount:

    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0

    def show_details(self):
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account1 = BankAccount("Abhinav", "12345")

account1.show_details()