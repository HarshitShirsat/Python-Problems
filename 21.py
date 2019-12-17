class Account():
    def __init__(self,a):
        self.__accno=a
        self.__bal=100
    def withdraw(self,amt):
        if (self.__bal-amt)<100:
            print("Low balance")
        else:
            self.__bal-=amt
    def deposit(self,amt):
        self.__bal+=amt
    def getAccno(self):
        return self.__accno
    def getBal(self):
        return self.__bal

cust=[]
test=1
while(test):
    print("1)New Account\n2)Deposit\n3)Withdraw\n4)Highest Balance\n5)Exit")
    op=int(input("Enter your choice - "))
    if(op==1):
        a=int(input("Enter account number - "))
        obj=Account(a)
        cust.append(obj)
    elif(op==2):
        a=int(input("Enter account number - "))
        for i in cust:
            if a==i.getAccno():
                amt=int(input("Enter amount to deposit - "))
                i.deposit(amt)
    elif(op==3):
        a=int(input("Enter account number - "))
        for i in cust:
            if a==i.getAccno():
                amt=int(input("Enter amount to deposit - "))
                i.withdraw(amt)
    elif(op==4):
        ballist=[]
        for i in cust:
            x=i.getBal()
            ballist.append(x)

        maxbal=ballist[0]
        for i in ballist:
            if i>maxbal:
                maxbal=i

        j=ballist.index(maxbal)
        print("Accno with highest balance - ",cust[j].getAccno())
    elif(op==5):
        test=0
    else:
        print("Invalid option")
