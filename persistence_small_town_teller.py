class person:

    def __init__(self, custid, first_name, last_name):
        self.custid = custid
        self.fname = first_name
        self.lname = last_name
          


class account:
    
    def __init__(self, number, actype, owner, balance):
        self.number = number
        self.type = actype
        self.owner = owner
        self.balance = balance
    
        

class bank:
    def __init__(self):
        pass

    def add_customer(self,newcust):
#        print(newcust.custid,newcust.fname,newcust.lname)
        customer.update({newcust.custid:(newcust.fname,newcust.lname)})

    def add_account(self,newaccount):
#        print(newaccount.number,newaccount.type,newaccount.owner.custid,newaccount.owner.fname, newaccount.owner.lname,newaccount.balance)
        accounts.update({newaccount.number:(newaccount.type,newaccount.owner,newaccount.balance)})

    def delete_account(self,delaccount):
        del accounts[delaccount]

    def deposit_money(self,account,amount):
        newbalance = accounts[account][2] + amount
        l1 = list(accounts[account])
        l1[2] = newbalance
        accounts[account] = tuple(l1)
        #print(accounts[account])

    def withdraw_money(self,account,amount):
        newbalance = accounts[account][2] - amount
        if newbalance > 0:
            l1 = list(accounts[account])
            l1[2] = newbalance
            accounts[account] = tuple(l1)
        else:
            print('Insufficient balance\n')
        print('Your new balance = ', accounts[account][2])

    def balance_inquiry(self,account):
        print("Your balance is - ", accounts[account][2])


#initial declaration
customer ={} # Create empty customer dictionary
accounts ={} # Create empty accounts dictionary
transact_bank = bank() # Create an object of Class Bank

#add customer 
customer1 = person(1,'preeti','sehgal')
transact_bank.add_customer(customer1)

#add account
account1 = account(1000,'savings',customer1,5000)
transact_bank.add_account(account1)

account2 = account(1001,'savings',customer1,5000)
transact_bank.add_account(account2)

#remove account
transact_bank.delete_account(account2.number)

#deposit money
transact_bank.deposit_money(account1.number, 3000)

#withdraw money
transact_bank.withdraw_money(account1.number, 2000)

#balance inquiry
transact_bank.balance_inquiry(account1.number)

 


        


