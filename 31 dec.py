#!/usr/bin/env python
# coding: utf-8

# In[1]:


#bank
class bank:
    def __init__(self):
        self.name='abc'
        self.accnum='342156'
        self.balance=3000 
    def info(self):
        print('name:',self.name)
        print('account num:',self.accnum) 
        print('balance:',self.balance)
    def deposite(self):
        amount=int(input("enter amt for deposite"))
        self.balance+=amount
    def withdraw(self):
        amount=int(input("enter amt for withdraw"))
        self.balance-=amount
    def transfer(self):
        amount=int(input("enter amt for transfer"))
        self.balance-=amount
        
    
        


# In[2]:


pin=int(input("enter pin"))
if(pin==9043):
    while(1):
        p1=bank()
        ch=int(input("enter your choice \n1.info\n2.deposite\n3.withdraw\n4.transfer\n5.exit"))
        if(ch==1):
            p1.info()
        elif(ch==2):
            p1.deposite()
            p1.info()
        elif(ch==3):
            p1.withdraw()
            p1.info()
        elif(ch==4):
            p1.transfer()
            p1.info()
        else:
            break
else :
        print("invalid pin")


# In[ ]:




