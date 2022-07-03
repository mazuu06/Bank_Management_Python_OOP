

class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TransferCash = False
        
    def register(self, name, ph, password):
        cash = self.cash
        condition = True
        
        if len(str(ph)) < 10 or len(str(ph)) > 10:
            print("Invalid phone number! Please enter 11 digit number")
            condition = False
            
        
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            condition = False
        
            
        if condition == True:
            print("Account created successfully")
            self.client_details_list = [name, ph, password, cash]
            with open (f"{name}.txt", "w+") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")
                    
    def login(self, name, ph, password):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True
                    
            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name
                
            else:
                print("Wrong details")
                exit()
     
    @property       
    def check_balance(self):
        with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
                Balance = self.client_details_list[3]
        return int(Balance)
                
    
    def add_cash(self, amount):
        if amount > 0:
            cash = self.check_balance 
            cash += amount
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n") 
                
            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(cash))) 
                
            print("Amount added successfully")
            
        else:
            print("Enter correct value of amount")
            
    def Transfer_cash(self, amount, name, ph):
        cash = self.check_balance
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TransferCash = True
                
        if self.TransferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = cash - amount
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))
 
            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")
                
            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))
            print("Amount Transfered Successfully to ", name,"-", ph)
            print("Balance left = ",left_cash)
            
    def password_change(self, password):
        if len(str(password)) < 5 or len(str(password)) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("New password set up successfully")
            
    def ph_chnage(self, ph):
        if len(str(ph)) < 10 or len(str(ph)) > 10:
            print("Invalid phone number! Please enter 11 digit number")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("New phone number set up successfully")
        
        
            
            
if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcomw to my Bank")
    print("1. Login")
    print("2. Create a new Account")
    user = int(input("Make Decision: "))
    if user == 1:
        print("Logging in......")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter Password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1. Add amount")
                print("2. Check Balance")
                print("3. Transfrt amount")
                print("4. Edit Profile")
                print("5. Logout")
                login_user = int(input("--> "))
                if login_user == 1:
                    print("Balance = ",Bank_object.check_balance)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1. Back menu")
                    print("2. Logout")
                    choose = int(input("--> "))
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                    
                elif login_user == 2:
                    print("Balance = ",Bank_object.check_balance)
                    print("\n1. Back menu")
                    print("2. Logout")
                    choose = int(input("--> "))
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                    
                elif login_user == 3:
                    print("Balance = ",Bank_object.check_balance)
                    amount = int(input("Enter amount: "))
                    if amount > 0 and amount <= Bank_object.check_balance:
                        name = input("Enter Person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Transfer_cash(amount, name, ph)
                        print("\n1. Back menu")
                        print("2. Logout")
                        choose = int(input("--> "))
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                        
                    elif amount <= 0:
                        print("Enter please correct value of amount")       
                    elif amount > Bank_object.check_balance:
                        print("Not enough balance")
                      
                
                elif login_user == 4:
                    print("1. Password change")
                    print("2. Phone No. change")
                    edit_profile = int(input("--> "))
                    if edit_profile == 1:
                        new_password = input("Enter new password: ")
                        Bank_object.password_change(new_password)
                        print("\n1. Back menu")
                        print("2. Logout")
                        choose = int(input("--> "))
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                        
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new phone number: "))
                        Bank_object.ph_chnage(new_ph)   
                        print("\n1. Back menu")
                        print("2. Logout")
                        choose = int(input("--> "))
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break  
                        
                elif login_user == 5:
                    break  
                
                else:
                    print("Wrong input")                
                        
                
    elif user == 2:
        print("Creating a new Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter Password: ")
        Bank_object.register(name, ph, password)
        
    else:
        print("Wrong input")
        
        
    